'''
The images module provides standard helper functions to explore and visualize images
'''

import logging
import os
import numpy as np
from cv2 import imread
from skimage import transform

_logger = logging.getLogger()

def load_images(path: str, image_size:int = -1, max_images: int = -1, 
                valid_extensions: np.array = ['.jpg','.jpeg','.gif','.png'],
                convert_to_grey: bool = False, keep_3d_shape = False) -> np.array:
    '''
    Loads the images from a specific folder
    Args:
        path (str): The path or folder name to load images from.  This can be a relative or fully qualified path
        image_size (int): If the image_size is larger than 0, the images will be resized to a square of this size
        max_images (int): The maximum amount of images to load from the folder.  If 0 or smaller, all images will be returned
        valid_extensions (np.array): The file extensions that should be filtered.  Defaults to jpg, jpeg, gif and png
        convert_to_grey (bool): This would reduce the size (and shape) of the image in making it a greyscale
        keep_3d_shape (bool): Only used when convert_to_grey is true.  Will keep the images in shape (H,W,1) in that case
    Returns: 
        np.array: A numpy array that contains all selected images represented as np.array
    '''
    images = []
    for f in os.listdir(path)[:]:
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_extensions:
            continue

        im = imread(os.path.join(path,f)) 
        if(image_size > 0):
            im = transform.resize(im,(image_size, image_size),mode='constant',anti_aliasing=True)

        if(convert_to_grey):
            if(len(im.shape) == 3):
                im = np.dot(im, [0.3, 0.59, 0.11])
            if(len(im.shape)==2 and keep_3d_shape):
                im = np.expand_dims(im, -1)

        images.append(im)
        if(len(images) >= max_images and max_images > 0):
            break
    
    return np.array(images)
