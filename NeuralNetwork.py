
import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot
import random
from random import shuffle
from sklearn import metrics
import time
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier
import speech_recognition as sr


for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print('Microphone with name {}'.format(name),
          'found for Microphone {}'.format(index))

r = sr.Recognizer()
r.dynamic_energy_Threshold = True
r.pause_threshold = 1.0

while True:
    with sr.Microphone(device_index = 0) as source:
        print("Speak: ")
        audio = r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print('You said: {}'.format(r.recognize_google(audio, language = 'en-US')))
        break
    except sr.UnknownValueError:
        print('Could you please repeat that?')
    except sr.RequestError as e:
        print('Could not request results: {}'.format(e))
