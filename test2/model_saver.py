# -*- coding: utf-8 -*-
"""
Created on Mon May  7 18:10:55 2018

@author: CHATHUWA
"""

#Import Libraries
import pandas as pd
import numpy as np

#Visualization Imports
import matplotlib.pyplot as plt
import seaborn as sns

#Load the dataset
medi_cost = pd.read_csv('extent.csv')

medi_cost.isnull()

#Preview of the dataset
medi_cost.head()

#Assign X,y values
X = medi_cost.iloc[:, :-1].values
y = medi_cost.iloc[:, 2].values


from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 0)

#Import Linear Regression
from sklearn.linear_model import LinearRegression

#Tran the dataset
regressor = LinearRegression()
regressor.fit(X_train, y_train)

from sklearn.externals import joblib
joblib.dump(regressor,'model.pkl')