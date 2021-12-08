<!-- markdownlint-disable -->

<a href="../../../arcus/ml/images/explorer.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `ml.images.explorer`
The image explorer module provides standard helper functions to explore and visualize images 


---

<a href="../../../arcus/ml/images/explorer.py#L14"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `show_image`

```python
show_image(
    image: <built-in function array>,
    hide_grid: bool = True,
    grid_size=None,
    silent_mode: bool = False
)
```

Visualizes an image 

**Args:**
 
 - <b>`image`</b> (np.array):  the image to visualize, represented as numpy array 
 - <b>`hide_grid`</b> (bool):  indicating if the grid (with the pixel positions) should be hidden 
 - <b>`grid_size`</b> ((int, int)):  the size of the grid to plot the images in.  By default auto size is being applied 
 - <b>`silent_mode`</b> (bool):  indicates if the image has to be plotted, or just returned 


---

<a href="../../../arcus/ml/images/explorer.py#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `visualize`

```python
visualize(
    image_sets: dict,
    image_count: int = 10,
    randomize: bool = True,
    grid_size=None,
    hide_grid: bool = True,
    silent_mode: bool = False
)
```

Visualizes the images in the image_sets in a grid 

**Args:**
 
 - <b>`image_sets`</b> (dict):  a dictionary of type (str, list) that indicates the name of an images set and the actual images 
 - <b>`image_count`</b> (int):  the amount of images to visualize from an image set 
 - <b>`randomize`</b> (bool):  if True, images will be selected randomly from the imageset, if False, the first n images will be taken 
 - <b>`grid_size`</b> ((int, int)):  the size of the grid to plot the images in.  By default auto size is being applied 
 - <b>`hide_grid`</b> (bool):  indicates if the grid with pixellocations should be hidden 
 - <b>`silent_mode`</b> (bool):  indicates if the image has to be plotted, or just returned 



**Example:**
 

image_sets = {'predicted': y_pred, 'actuals': y_test} 

visualize(image_sets, 6, False) 


---

<a href="../../../arcus/ml/images/explorer.py#L93"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `visualize_classes`

```python
visualize_classes(
    image_set: <built-in function array>,
    classes: <built-in function array>,
    image_count: int = 10,
    randomize: bool = True,
    grid_size=None,
    silent_mode: bool = False
)
```

Visualizes the images from the image_set in a grid and print the corresponding class on the charts 



**Args:**
 
 - <b>`image_set`</b> (np.array):  an array of images to pick from 
 - <b>`classes`</b> (np.array):  the corresponding labels of the classes for the images 
 - <b>`image_count`</b> (int):  the amount of images to visualize from an image set 
 - <b>`randomize`</b> (bool):  if True, images will be selected randomly from the imageset, if False, the first n images will be taken 
 - <b>`grid_size`</b> ((int, int)):  the size of the grid to plot the images in.  By default auto size is being applied 
 - <b>`silent_mode`</b> (bool):  indicates if the image has to be plotted, or just returned 



**Example:**
 

image_sets = {'predicted': y_pred, 'actuals': y_test} 

visualize(image_sets, 6, False) 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
