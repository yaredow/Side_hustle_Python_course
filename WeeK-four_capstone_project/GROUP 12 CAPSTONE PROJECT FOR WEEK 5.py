# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 01:51:35 2021

@author: USER
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:/Users/USER/Desktop/personal development/SIDE HUSTLE PYTHON/Student_data.csv')
# independent variable is score
x = data.iloc[:,1].values
#dependent variable is the level of intelligenc
y = data.iloc[:,2].values

#splitting to train and test data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,train_size = 0.85)

#importing sklearn model
x_train   =x_train.reshape(-1,1)
y_train =y_train.reshape(-1,1)
x_test =x_test.reshape(-1,1)
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(x_train,y_train)
# testing the linear regression model with test data
y_predtest = reg.predict(x_test)
y_predtrain = reg.predict(x_train)

#visualizing the train data
plt.scatter(x_train,y_train)
plt.plot (x_train,y_predtrain,color = 'red')
plt.title('level of intelligence against the score(train data)')
plt.xlabel('scores')
plt.ylabel('level of intelligence')
plt.show()

#visualizing the test data
plt.scatter(x_test,y_test)
plt.plot (x_test,y_predtest,color = 'black')
plt.title('level of intelligence against the score(test data)')
plt.xlabel('scores')
plt.ylabel('level of intelligence')
plt.show()