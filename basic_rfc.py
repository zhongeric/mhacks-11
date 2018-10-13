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

# INITIALIZE HERE
np.random.seed(1)

sample_words = ['pump']

df = pd.read_csv('sample_words.csv')

# Pull labels, drop labels
Y = df['Step']
df = df.drop('Step', 1)

# dummy_data = pd.get_dummies(df['Input'])
# new_df = pd.concat([df, dummy_data], axis=1)
# new_df = new_df.drop('Input', 1)
#
# print(new_df)
le = LabelEncoder()
#Auto encodes any dataframe column of type category or object.
def dummyEncode(df):
        columnsToEncode = list(df.select_dtypes(include=['category','object']))
        for feature in columnsToEncode:
            try:
                df[feature] = le.fit_transform(df[feature])
            except:
                print('Error encoding '+feature)
        return df

new_df = dummyEncode(df)
print(new_df)
X = new_df
categories = list(X.columns)

print('The shape of our features is:', new_df.shape)

def getAccuracy(pre,ytest):
    count = 0
    for i in range(len(ytest)):
        if ytest[i]==pre[i]:
            count+=1
    acc = float(count)/len(ytest)
    return acc

#Extract data values from the data frame
feat = new_df.keys()
feat_labels = new_df.get_values()

from sklearn.model_selection import train_test_split
# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(new_df, Y, test_size = 0.25, random_state = 42)

print('Training Features Shape:', X_train.shape)
print('Training Labels Shape:', Y_train.shape)
print('Testing Features Shape:', X_test.shape)
print('Testing Labels Shape:', Y_test.shape)

clf = RandomForestClassifier()

clf.fit(X_train, Y_train)

pre = clf.predict(X_test)

# Get probability predictions
Y_array = pd.np.array(Y_test)

acc = getAccuracy(pre, Y_array)

# color_input = input("What color is the fruit? ")
# shape_input = input("What shape is the fruit? (sphere or naw) ")
# taste_input = input("Is the fruit sweet or sour? ")
d = {'Input': ['pump']}
given_df = pd.DataFrame(data=d)
g = dummyEncode(given_df)
print(g)
given_pre = clf.predict(g).reshape(1,-1)
decoded_pre = le.inverse_transform(given_pre[0])
print(given_pre)
print(decoded_pre)
print(acc)
