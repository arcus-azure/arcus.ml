<!-- markdownlint-disable -->

<a href="../../../arcus/ml/evaluation/classification.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `ml.evaluation.classification`
The classification module allows users to evaluate and visualize classifiers 


---

<a href="../../../arcus/ml/evaluation/classification.py#L13"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `evaluate_model`

```python
evaluate_model(
    fitted_model,
    X_test: <built-in function array>,
    y_test: <built-in function array>,
    show_roc: bool = False
) → <built-in function array>
```

Will predict and evaluate a model against a test set 



**Args:**
 
 - <b>`fitted_model`</b> (model):  The already fitted model to be tested.  Sklearn and Keras models have been tested 
 - <b>`X_test`</b> (np.array):  The test set to calculate the predictions with 
 - <b>`y_test`</b> (np.array):  The output test set to evaluate the predictions against 
 - <b>`show_roc`</b> (bool):  This will plot the ROC curve in case of a binary classifier 



**Returns:**
 
 - <b>`np.array`</b>:  The predicted (y_pred) values against the model 


---

<a href="../../../arcus/ml/evaluation/classification.py#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_roc_curve`

```python
plot_roc_curve(
    y_pred: <built-in function array>,
    y_test: <built-in function array>
)
```

Will plot the Receiver Operating Characteristic (ROC) Curve for binary classifiers 



**Args:**
 
 - <b>`y_pred`</b> (np.array):  The predicted values of the test set  
 - <b>`y_test`</b> (np.array):  The actual outputs of the test set 



**Returns:**
 
 - <b>`float`</b>:  The ROC_AUC value 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
