'''
The classification module allows users to evaluate and visualize classifiers
'''

import logging
import os
import numpy as np
import sklearn.metrics as metrics
import matplotlib.pyplot as plt

_logger = logging.getLogger()   

def evaluate_model(fitted_model, X_test: np.array, y_test: np.array, show_roc: bool = False) -> np.array:
    '''Will predict and evaluate a model against a test set

    Args:
        fitted_model (model): The already fitted model to be tested.  Sklearn and Keras models have been tested
        X_test (np.array): The test set to calculate the predictions with
        y_test (np.array): The output test set to evaluate the predictions against
        show_roc (bool): This will plot the ROC curve in case of a binary classifier

    Returns: 
        np.array: The predicted (y_pred) values against the model
    '''
    y_pred = fitted_model.predict(X_test)
    print(metrics.classification_report(y_test, y_pred))

    cf = metrics.confusion_matrix(y_test, y_pred)
    print(cf)
    accuracy = metrics.accuracy_score(y_test, y_pred) * 100
    print('Accuracy score:', accuracy) 
    if(show_roc == True):
        # Verify that we are having a binary classifier
        if(len(fitted_model.classes_)!=2):
            raise AttributeError('Showing a ROC curve is only possible for binary classifier, not for multi class')
        plot_roc_curve(y_test, y_pred) 
    
    return y_pred

def plot_roc_curve(y_pred: np.array, y_test: np.array):
    '''Will plot the Receiver Operating Characteristic (ROC) Curve for binary classifiers

    Args:
        y_pred (np.array): The predicted values of the test set 
        y_test (np.array): The actual outputs of the test set

    Returns: 
        float: The ROC_AUC value
    '''
    # calculate the fpr and tpr for all thresholds of the classification
    fpr, tpr, threshold = metrics.roc_curve(y_test, y_pred)
    roc_auc = metrics.auc(fpr, tpr)

    plt.title('Receiver Operating Characteristic')
    plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
    plt.legend(loc = 'lower right')
    plt.plot([0, 1], [0, 1],'r--')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.show()
    return roc_auc