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

def keywordsfrominstructions(text_file):
    line_keywords = []
    with open(text_file) as inputfile:
        for line in inputfile:
            line_keywords.append(filter(line))

    keywords_cpr = []
    for i in range(len(line_keywords)):
        keywords_cpr.append(' '.join([word.replace("'", "") for word in line_keywords[i]]))

    total_wordlist = []
    for i in range(len(keywords_cpr)):
        wordlist = re.sub('[' + string.punctuation + ']', " ", keywords_cpr[i]).split()
        for word in wordlist:
            if word == 's' or word.isdigit():
                wordlist.remove(word)
        total_wordlist.append(wordlist)

    total_synonyms = []
    synonyms_by_line = []
    for j, line in enumerate(total_wordlist):
        for word in line:
            for syn in wordnet.synsets(word)[1:4]:
                for lm in syn.lemmas()[:3]:
                    synonyms_by_line.append(lm.name())
        total_synonyms.append(synonyms_by_line)
        synonyms_by_line = []


    for k in range(len(total_wordlist)):
        for word in total_synonyms[k]:
            total_wordlist[k].append(word)

    final = []
    for l in range(len(total_wordlist)):
        final.append(' '.join(total_wordlist[l]))

    final_keywords = pd.Series(final)
    final_values = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    final_dataset = pd.concat([final_keywords, final_values], axis = 1)

    return final_dataset

adult_wordlist = keywordsfrominstructions('cpradult.txt')
child_wordlist = keywordsfrominstructions('cprchild.txt')
infant_wordlist = keywordsfrominstructions('cprinfant.txt')

adult_wordlist.to_csv('training_data_adult.csv')
child_wordlist.to_csv('training_data_child.csv')
infant_wordlist.to_csv('training_data_infant.csv')
