
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

# audio_string = audio_text(device_index = 0)
# filtered_string = filter(audio_string)

def keywordsfrominstructions(text_file):
    line_keywords = []
    with open(text_file) as inputfile:
        for line in inputfile:
            line_keywords.append(filter(line))

    keywords_cpr = []
    for i in range(len(line_keywords)):
        keywords_cpr.append(' '.join([word.replace("'", "") for word in line_keywords[i]]))

    for i in range(len(keywords_cpr)):
        wordlist = re.sub('[' + string.punctuation + ']', " ", keywords_cpr[i]).split()
        for word in wordlist:
            if word == 's' or word.isdigit():
                wordlist.remove(word)
        for word in wordlist:
            for syn in wordnet.synsets(word):
                for lm in syn.lemmas():
                    wordlist += lm.name()

        final_keywords = []
        for j in range(len(wordlist)):
            final_keywords.append((' '.join([word.replace("'", "") for word in wordlist[j]])) + ',' + str(i+1))

    return final_keywords

def main():
    adult_wordlist = keywordsfrominstructions('cpradult.txt')
    child_wordlist = keywordsfrominstructions('cprchild.txt')
    infant_wordlist = keywordsfrominstructions('cprinfant.txt')

    print(adult_wordlist)
    
if __name__ = '__main__':
    main()
