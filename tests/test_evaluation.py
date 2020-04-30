import sys
import os
import pytest
import pandas as pd 
import logging
import numpy as np
from unittest.mock import patch 
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from arcus.ml.evaluation import classification as clev

def test_binary_classifier_evaluation():
    df = pd.read_csv('tests/resources/datasets/student-admission.csv')
    y = df.Admission.values
    X = np.asarray(df.drop(['Admission'],axis=1))
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

    # trainen van de logistic regression classifier
    logreg = linear_model.LogisticRegression(C=1e5,solver='liblinear')
    logreg.fit(X_train, y_train)
    clev.evaluate_model(logreg, X_test, y_test)

@patch("matplotlib.pyplot.show")
def test_binary_classifier_evaluation_roc(mock_show):
    df = pd.read_csv('tests/resources/datasets/student-admission.csv')
    y = df.Admission.values
    X = np.asarray(df.drop(['Admission'],axis=1))
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

    # trainen van de logistic regression classifier
    logreg = linear_model.LogisticRegression(C=1e5,solver='liblinear')
    logreg.fit(X_train, y_train)
    clev.evaluate_model(logreg, X_test, y_test, True)
    

def test_multiclass_classifier_evaluation_roc():
    df = pd.read_csv('tests/resources/datasets/wine-makers.csv')
    y = df.Cultivar.values
    X = df.drop(['Cultivar'],axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

        # trainen van de logistic regression classifier
    logreg = linear_model.LogisticRegression(C=1,solver='lbfgs')
    logreg.fit(X_train, y_train)
    # We are trying to apply the Roc curve for a multi class classifier
    # This should raise an exception
    with pytest.raises(AttributeError) as attribute_err:
        clev.evaluate_model(logreg, X_test, y_test, True)
    assert 'binary classifier' in str(attribute_err.value)

def test_multiclass_classifier_evaluation_noroc():
    df = pd.read_csv('tests/resources/datasets/wine-makers.csv')
    y = df.Cultivar.values
    X = df.drop(['Cultivar'],axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

        # trainen van de logistic regression classifier
    logreg = linear_model.LogisticRegression(C=1,solver='lbfgs')
    logreg.fit(X_train, y_train)

    clev.evaluate_model(logreg, X_test, y_test, False)
