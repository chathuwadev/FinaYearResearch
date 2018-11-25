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

#Predict the values using test dataset
y_pred = regressor.predict(X_test)


y_pred_16_jan = regressor.predict([[313.17647

,2.076923077

]])

y_pred_16_feb = regressor.predict([[307.17647

,1.233333333

]])

y_pred_16_mar = regressor.predict([[102.5

,1.413043478

]])

y_pred_16_apr = regressor.predict([[49.8

,2.681868132

]])
y_pred_16_may = regressor.predict([[51.411764

,4.419565217

]])

y_pred_16_jun = regressor.predict([[89.058823

,4.354347826

]])

y_pred_16_jul = regressor.predict([[366.705882

,2.98423913

]])

y_pred_16_aug = regressor.predict([[637.823529

,1.810869565

]])

y_pred_16_sep = regressor.predict([[461.470588

,3.110989011

]])

y_pred_16_oct = regressor.predict([[90.764705

,3.751086957

]])

dfs=pd.read_csv('potato.csv')
dfs.plot(x="Month",y=["Actual","Predict"],kind="line")

