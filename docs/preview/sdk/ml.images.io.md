<!-- markdownlint-disable -->

<a href="../../../arcus/ml/images/io.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `ml.images.io`
The io module provides standard helper functions to load images from disk 

**Global Variables**
---------------
- **IMREAD_COLOR**

---

<a href="../../../arcus/ml/images/io.py#L18"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `load_image_from_disk`

```python
load_image_from_disk(
    path: str,
    image_size=None,
    convert_to_grey: bool = False,
    keep_3d_shape=False
) → <built-in function array>
```

Loads an image from file, applying preformatting 

**Args:**
 
 - <b>`path`</b> (str):  The filename of the image to load 
 - <b>`image_size`</b> (tuple):  The image size can be passed as tuple (W, H) or as int (W=H) 
 - <b>`convert_to_grey`</b> (bool):  This would reduce the size (and shape) of the image in making it a greyscale 
 - <b>`keep_3d_shape`</b> (bool):  Only used when convert_to_grey is true.  Will keep the images in shape (H,W,1) in that case 

**Returns:**
 
 - <b>`np.array`</b>:  A numpy array that represents the image 


---

<a href="../../../arcus/ml/images/io.py#L35"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `load_images`

```python
load_images(
    path: str,
    image_size=None,
    max_images: int = -1,
    valid_extensions: <built-in function array> = ['.jpg', '.jpeg', '.gif', '.png'],
    convert_to_grey: bool = False,
    keep_3d_shape=False
) → <built-in function array>
```

Loads the images from a specific folder 

**Args:**
 
 - <b>`path`</b> (str):  The path or folder name to load images from.  This can be a relative or fully qualified path 
 - <b>`image_size`</b> (tuple):  The image size can be passed as tuple (W, H) or as int (W=H) 
 - <b>`max_images`</b> (int):  The maximum amount of images to load from the folder.  If 0 or smaller, all images will be returned 
 - <b>`valid_extensions`</b> (np.array):  The file extensions that should be filtered.  Defaults to jpg, jpeg, gif and png 
 - <b>`convert_to_grey`</b> (bool):  This would reduce the size (and shape) of the image in making it a greyscale 
 - <b>`keep_3d_shape`</b> (bool):  Only used when convert_to_grey is true.  Will keep the images in shape (H,W,1) in that case 

**Returns:**
 
 - <b>`np.array`</b>:  A numpy array that contains all selected images represented as np.array 


---

<a href="../../../arcus/ml/images/io.py#L64"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `load_image_from_url`

```python
load_image_from_url(
    image_url: str,
    http_headers: dict = None,
    image_size=None,
    convert_to_grey: bool = False,
    keep_3d_shape=False,
    cache_location: str = None,
    file_name: str = None,
    force_download: bool = False
) → <built-in function array>
```

Loads an image from a given url, applying preformatting and supporting file caching 

**Args:**
 
 - <b>`image_url`</b> (str):  The url to download the image. 
 - <b>`http_headers`</b> (dict):  The http headers to pass with the request as a dictionary 
 - <b>`image_size`</b> (tuple):  The image size can be passed as tuple (W, H) or as int (W=H) 
 - <b>`convert_to_grey`</b> (bool):  This would reduce the size (and shape) of the image in making it a greyscale 
 - <b>`keep_3d_shape`</b> (bool):  Only used when convert_to_grey is true.  Will keep the images in shape (H,W,1) in that case 
 - <b>`cache_location`</b> (str):  When provided, the image will be cached to this folder location on disk 
 - <b>`file_name`</b> (str):  The file name of the image to be cached 
 - <b>`force_download`</b> (bool):  When true, the image will always be redownloaded and not retrieved from cache 

**Returns:**
 
 - <b>`np.array`</b>:  A numpy array that represents the image 


---

<a href="../../../arcus/ml/images/io.py#L117"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `load_images_from_dataframe`

```python
load_images_from_dataframe(
    df: DataFrame,
    image_column_name: str,
    target_column_name: str,
    image_size=None,
    max_images: int = -1,
    target_as_image: bool = False,
    convert_to_grey: bool = False,
    keep_3d_shape=False
) → (<built-in function array>, <built-in function array>)
```

Loads a set images from disk, based on the file name in a Data Frame.   And returns a related array (target) that can contain values from another column, or also images from disk 



**Args:**
 
 - <b>`df`</b> (pd.DataFrame):  the DataFrame, containing the references to the image 
 - <b>`image_column_name`</b> (str):  The name of the column that contains the image reference 
 - <b>`target_column_name`</b> (str):  The name of the column that contains the related target data 
 - <b>`image_size`</b> (tuple):  The image size can be passed as tuple (W, H) or as int (W=H) 
 - <b>`max_images`</b> (int):  The maximum amount of images to load from the folder.  If 0 or smaller, all images will be returned 
 - <b>`target_as_image`</b> (bool):  Defines if the target column contains file names that should be loaded as image.  If not, the column data will be used in the target array 
 - <b>`convert_to_grey`</b> (bool):  This would reduce the size (and shape) of the image in making it a greyscale 
 - <b>`keep_3d_shape`</b> (bool):  Only used when convert_to_grey is true.  Will keep the images in shape (H,W,1) in that case 



**Returns:**
 a tuple with the following objects: 
 - <b>`np.array`</b>:  A numpy array that contains all selected images represented as np.array 
 - <b>`np.array`</b>:  A numpy array that represents all targets that were asked 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
