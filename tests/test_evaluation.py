import sys
import os
import pytest
import pandas as pd 
import logging
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from arcus.ml.evaluation import classification as clev

def test_linear_regression_evaluation():
    df = pd.read_csv('tests/resources/datasets/student-admission.csv')
    y = df.Admission.values
    X = np.asarray(df.drop(['Admission'],axis=1))
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

    # trainen van de logistic regression classifier
    logreg = linear_model.LogisticRegression(C=1e5,solver='liblinear')
    logreg.fit(X_train, y_train)
    clev.evaluate_model(logreg, X_test, y_test)
    