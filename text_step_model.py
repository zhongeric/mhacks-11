from sklearn.feature_selection import SelectFromModel
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from random import shuffle
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics
import coremltools
import time
import pickle

from textblob import TextBlob

# train = [
#       ('The man is lying on the ground', '1'),
#       ('The man cannot breathe', '1'),
#       ('The man is unconcious', '1'),
#       ('I just did 30 pumps', '2'),
#       ("What do I do next", 'B'),
#       ('Im stuck', 'B'),
# ]

# test = [
#       ('They are on the ground', '1'),
#       ('I dont think they can breath', '1'),
#       ('They are not responding', '1'),
#       ('50 pumps finished', '2'),
#       ("Next Step", 'B'),
#       ('Im stuck', 'B'),
# ]

from textblob.classifiers import NaiveBayesClassifier
with open('cpradult.csv', 'r') as fp:
    cl = NaiveBayesClassifier(fp, format="csv")

pred = cl.prob_classify("I just put them on their back")
print(pred.max())
print(pred.prob(pred.max()))
prob_dist = cl.prob_classify("i dont know what to do")
print(prob_dist.max())
print(prob_dist.prob(prob_dist.max()))

filename = 'text_to_step.pkl'
pickle.dump(cl, open(filename, 'wb'))

print("successfuly saved model")
