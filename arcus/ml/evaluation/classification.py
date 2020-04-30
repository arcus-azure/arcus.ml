'''
The classification module allows users to evaluate and visualize classifiers
'''

import logging
import os
import numpy as np
import sklearn.metrics as metrics
import matplotlib.pyplot as plt

_logger = logging.getLogger()   

def evaluate_model(fitted_model, X_test: np.array, y_test: np.array, show_roc: bool = False):
    y_pred = fitted_model.predict(X_test)
    print(metrics.classification_report(y_test, y_pred))

    cf = metrics.confusion_matrix(y_test, y_pred)
    print(cf)
    accuracy = metrics.accuracy_score(y_test, y_pred) * 100
    print('Accuracy score:', accuracy) 
    if(show_roc == True):
        plot_roc_curve(y_test, y_pred) 

def plot_roc_curve(y_pred: np.array, y_test: np.array):
    # calculate the fpr and tpr for all thresholds of the classification
    fpr, tpr, threshold = metrics.roc_curve(y_test, y_pred)
    roc_auc = metrics.auc(fpr, tpr)

    plt.title('Receiver Operating Characteristic')
    plt.plot(fpr, tpr, 'b', label = 'Area under the Curve = %0.2f' % roc_auc)
    plt.legend(loc = 'lower right')
    plt.plot([0, 1], [0, 1],'r--')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.show()