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
import objc
import pyttsx3

with open('training_data_adult.csv', 'r') as fp:
    cladult = NaiveBayesClassifier(fp, format="csv")

with open('training_data_child.csv', 'r') as fp:
    clchild = NaiveBayesClassifier(fp, format="csv")

with open('training_data_infant.csv', 'r') as fp:
    clinfant = NaiveBayesClassifier(fp, format="csv")

while True:
    audio_string = audio_text(device_index = 0)
    audio_string = filter(audio_string)

    if 'adult' in audio_string:
        pred = cladult.prob_classify(audio_string)
        break
    elif 'child' in audio_string:
        pred = clchild.prob_classify(audio_string)
        break
    elif 'infant' in audio_string:
        pred = clinfant.prob_classify(audio_string)
        break
    else:
        print('You did not provide the age of the person')


print('Your predicted class is {}'.format(pred.max()))
print('Your predicted probability is {}'.format(pred.prob(pred.max())))
