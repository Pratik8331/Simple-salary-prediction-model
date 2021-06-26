# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 00:28:24 2021

@author: Pratik
"""

# Linear Regression

import pandas as pd

dataset = pd.read_csv(r"C:\Users\Pratik Ranjan Raul\Desktop\Salary Dataset.csv")
X = dataset.iloc[:, :1].values
y = dataset.iloc[:,1:].values

# Splitting data for training and testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=2/3, random_state=0)

# Processing training Data
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting from test data
y_pred = regressor.predict(X_test)

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test,y_pred)
print('The mean squared error is ',mse)

# Plotting the Training Data
import matplotlib.pyplot as plt
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Plotting the Training Data
import matplotlib.pyplot as plt
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

new_salary_pred = regressor.predict([[15]])
print('The predicted salary of a person with 15 years experience is ',new_salary_pred)







