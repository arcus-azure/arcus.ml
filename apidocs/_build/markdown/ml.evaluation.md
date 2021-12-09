# ml.evaluation package

## Submodules

## ml.evaluation.classification module

The classification module allows users to evaluate and visualize classifiers


### ml.evaluation.classification.evaluate_model(fitted_model, X_test: numpy.array, y_test: numpy.array, show_roc: bool = False)
Will predict and evaluate a model against a test set


* **Parameters**

    
    * **fitted_model** (*model*) – The already fitted model to be tested.  Sklearn and Keras models have been tested


    * **X_test** (*np.array*) – The test set to calculate the predictions with


    * **y_test** (*np.array*) – The output test set to evaluate the predictions against


    * **show_roc** (*bool*) – This will plot the ROC curve in case of a binary classifier



* **Returns**

    The predicted (y_pred) values against the model



* **Return type**

    np.array



### ml.evaluation.classification.plot_roc_curve(y_pred: numpy.array, y_test: numpy.array)
Will plot the Receiver Operating Characteristic (ROC) Curve for binary classifiers


* **Parameters**

    
    * **y_pred** (*np.array*) – The predicted values of the test set


    * **y_test** (*np.array*) – The actual outputs of the test set



* **Returns**

    The ROC_AUC value



* **Return type**

    float


## Module contents
