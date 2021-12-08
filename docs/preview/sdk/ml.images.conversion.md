<!-- markdownlint-disable -->

<a href="../../../arcus/ml/images/conversion.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `ml.images.conversion`
The conversion module allows users to transform images freely 


---

<a href="../../../arcus/ml/images/conversion.py#L13"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `to_blackwhite`

```python
to_blackwhite(
    image_list: <built-in function array>,
    threshold=128,
    keep_3d_shape=False
) → <built-in function array>
```

Transforms an image to a black & white image 

**Args:**
 
 - <b>`image_list`</b> (np.array):  A numpy array that contains all selected images represented as np.array 
 - <b>`threshold`</b> (int):  The threshold (between 0 and 255) that decides a pixel will be 0 or 255 (W/B) 

**Returns:**
 
 - <b>`np.array`</b>:  A numpy array that contains all black & white images represented as np.array 


---

<a href="../../../arcus/ml/images/conversion.py#L39"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `prepare`

```python
prepare(
    image: <built-in function array>,
    image_size=None,
    convert_to_grey: bool = False,
    keep_3d_shape=False
) → <built-in function array>
```

Takes an image and applies preformatting 

**Args:**
 
 - <b>`image`</b> (np.array):  The array representation of the image to process 
 - <b>`image_size`</b> (tuple):  The image size can be passed as tuple (W, H) or as int (W=H) 
 - <b>`convert_to_grey`</b> (bool):  This would reduce the size (and shape) of the image in making it a greyscale 
 - <b>`keep_3d_shape`</b> (bool):  Only used when convert_to_grey is true.  Will keep the images in shape (H,W,1) in that case 

**Returns:**
 
 - <b>`np.array`</b>:  A numpy array that represents the preprocessed image 


---

<a href="../../../arcus/ml/images/conversion.py#L66"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `crop`

```python
crop(
    image: <built-in function array>,
    x: int,
    y: int,
    width: int,
    height: int
) → <built-in function array>
```

Crops an image based on the specified size 

**Args:**
 
 - <b>`image`</b> (np.array):  The array representation of the image to crop 
 - <b>`x`</b> (int):  The x coordinate of the rectangle to keep (horizontal position from the left) 
 - <b>`y`</b> (int):  The y coordinate of the rectangle to keep (vertical position from the top) 
 - <b>`width`</b> (int):  The width of the cropped image 
 - <b>`height`</b> (int):  The height of the cropped image 

**Returns:**
 
 - <b>`np.array`</b>:  A numpy array that represents the cropped part of the image 


---

<a href="../../../arcus/ml/images/conversion.py#L80"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_fragments`

```python
get_fragments(
    image: <built-in function array>,
    stride: tuple = (1, 1),
    fragment_size: tuple = (1, 1),
    rectangle=None
)
```

Scans an image and return the resulted parts as a list of image sections 

**Args:**
 
 - <b>`image`</b> (np.array):  The array representation of the image to scan 
 - <b>`stride`</b> (tuple):  The steps to move over the image 
 - <b>`fragment_size`</b> (tuple):  The size of the fragments to take from the image 
 - <b>`rectangle`</b> (np.array):  The rectangle in the image to scan (if only a part of the image should be scanned.  Form: (x, y, width, height) 

**Returns:**
 
 - <b>`np.array`</b>:  A numpy array that contains all fragments as images 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
