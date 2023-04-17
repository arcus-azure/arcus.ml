---
title: "Image interaction"
layout: default
---

# Image interaction
The Arcus ML library provides a Python module called `arcus.ml.images` which contains several ready-to-use functions to experiment with images during ML development.

## Image IO
The library provides simple ways for loading images into usable Numpy arrays.

```python
import arcus.ml.images.io as ami

# Loading image from disk
image = ami.load_image_from_disk('samples/images/lungs/CHNCXR_0001_0.png')

# Loads image from URL
image = ami.load_image_from_url(
    'https://charting.vwdservices.com/tchart/tchart.aspx?user=Tijdnet&issue=360017012&layout=gradient-v1&startdate=3Y&enddate=today&res=endofday&width=876&height=400&format=image/png&culture=nl-BE')
```

Other arguments and functions are available, like loading images from a Panda dataframe. See the [sdk API reference](../03-sdk/ml.images.io.md) for more information.

To further experiment with image interactions, see our [image Jupyter note book](https://github.com/arcus-azure/arcus.ml/blob/master/samples/images_operations.ipynb).

## Image conversion
Transforming images is especially useful when preparing a raw set of images as a clear ML dataset. The Arcus ML library provides several conversions functions functions to help you with this task.

First, the image(s) needs to be loaded into Numpy arrays. This can easily be done with one of our [image IO functions](#image-io).

### Black/white conversion
Converting images to black/white variants can help simplify the dataset for easier pattern-detection. The following example shows how a set of lungs can be converted to their black/white variants:

```python
import arcus.ml.images.io as ami
import arucs.ml.images.conversion as conv

image_path = 'tests/resources/images/lungs'
image_list = ami.load_images(image_path)

# Convert images to black/white variant for easier pattern-detection.
images_converted = conv.to_blackwhite(image_list)
```

The result of this conversion example:

![Lung without mask](/media/CHNCXR_0001_0.png)
![Lung with mask](/media/CHNCXR_0001_0_mask.png)

Other arguments and functions are available, like image cropping and image fragmentation. See the [sdk API reference](../03-sdk/ml.images.conversion.md) for more information.

To further experiment with image interactions, see our [image Jupyter note book](https://github.com/arcus-azure/arcus.ml/blob/master/samples/images_operations.ipynb).

## Image explorer
Visualizing images is a necessary task when experimenting with datasets and their outcome. The Arcus ML library provides several plotting functions to visualize images.

First, the image(s) needs to be loaded into Numpy arrays. This can easily be done with one of our [image IO functions](#image-io).

### Randomly visualize images in a grid
The library can visualize as set of images in a grid to more easily compare images and possible conversions made on its data.

The example below shows how multiple sets of images can be combined a visualization grid:

```python
lungs = io.load_images('/resources/images/lungs', max_images=10, convert_to_grey=True, keep_3d_shape=True)
masks = io.load_images('/resources/images/lungmasks', max_images=10, convert_to_grey=False)

explorer.visualize({'lungs': lungs, 'masks': masks}, image_count=5, grid_size=(20, 8), hide_grid=False)
```

The result of this visualization example:
![Lung and its mask visualization](/media/visualize-lung-and-masks.png)

To further experiment with image interactions, see our [image Jupyter note book](https://github.com/arcus-azure/arcus.ml/blob/master/samples/images_operations.ipynb).