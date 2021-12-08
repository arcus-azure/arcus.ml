<!-- markdownlint-disable -->

<a href="../../../arcus/ml/neuralnetworks/keras.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `ml.neuralnetworks.keras`
The keras module provides additions to work and visualize Keras neural networks 


---

<a href="../../../arcus/ml/neuralnetworks/keras.py#L12"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `enable_gpu`

```python
enable_gpu() → bool
```

Enables Keras to run on the GPU First it checks if there's a "physical device" available of type GPU If not, it will try to leverage plaidml for GPU enabling 



**Returns:**
 
 - <b>`bool`</b>:  A boolean value indicating if the GPU enablement succeeded 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
