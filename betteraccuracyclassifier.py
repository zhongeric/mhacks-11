import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot
import string
import random
from random import shuffle
from sklearn import metrics
import time
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import speech_recognition as sr
from audiototext import audio_text
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordfilter import filter
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from nltk.corpus import wordnet
import re
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier

def train_SGDclassifier(training_dataset, testing_dataset):
    training_dataset = pd.read_csv(training_dataset, header = None, names = ['steps', 'labels'])
    testing_dataset = pd.read_csv(testing_dataset, header = None, names = ['steps', 'labels'])

    count_vect = CountVectorizer()
    train_counts = count_vect.fit_transform(training_dataset.steps)

    tfidf_transformer = TfidfTransformer()
    train_features = tfidf_transformer.fit_transform(train_counts)

    text_clf_svm = Pipeline([('vect', CountVectorizer(stop_words = 'english')), ('tfidf', TfidfTransformer()),
                          ('clf', SGDClassifier(loss='log', penalty='l2', alpha=1e-3, max_iter=5,
                           random_state = 42, shuffle = True))])
    _ = text_clf_svm.fit(training_dataset.steps, training_dataset.labels)

    predicted_svm = text_clf_svm.predict(testing_dataset.steps)
    accuracy = np.mean(predicted_svm == testing_dataset.labels)

    return text_clf_svm, predicted_svm, accuracy

def main():
    cladult, adult_predicted_svm, adult_accuracy = train_SGDclassifier('cpradult.csv', 'testing_data_adult.csv')
    clchild, child_predicted_svm, child_accuracy = train_SGDclassifier('cprchild.csv', 'testing_data_child.csv')
    clinfant, infant_predicted_svm, infant_accuracy = train_SGDclassifier('cprinfant.csv', 'testing_data_infant.csv')

    print('Adult Accuracy: ', adult_accuracy, 'Child Accuracy: ', child_accuracy,
          'Infant Accuracy: ', infant_accuracy)

    while True:
        audio_string = audio_text(device_index = 0)
        audio_string = filter(audio_string)
        audio_string = ' '.join(audio_string)

        if 'adult' in audio_string:
            pred = cladult.predict(pd.Series(audio_string))
            prob = cladult.predict_proba(pd.Series(audio_string))[:, (pred-1)]
            break
        elif 'child' in audio_string:
            pred = clchild.predict(pd.Series(audio_string))
            prob = clchild.predict_proba(pd.Series(audio_string))[:, (pred-1)]
            break
        elif 'infant' in audio_string:
            pred = clinfant.predict(pd.Series(audio_string))
            prob = clinfant.predict_proba(pd.Series(audio_string))[:, (pred-1)]
            break
        else:
            print('You did not provide the age of the person')

    print('Your predicted class is {}'.format(pred))
    print('Your predicted probability is {}'.format(prob))

if __name__ = '__main__':
    main()

# parameters = {'vect_ngram_range': [(1, 1), (1, 2)], 'tfidf_use_idf': (True, False),
#               'clf_alpha': (1e-2, 1e-3)}
#
# gs_clf = GridSearchCV(text_clf, parameters, n_jobs = -1, cv=5)
# gs_clf = gs_clf.fit(adult_training_dataset.steps, adult_training_dataset.labels)
#
# print('Best score: ' + gs_clf.best_score)
# print('Best Params: ' + gs_clf.best_params_)
