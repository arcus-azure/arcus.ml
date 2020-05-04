'''
The io module provides standard helper functions to load images from disk
'''

import logging
import os
import numpy as np
from cv2 import imread, imdecode, IMREAD_COLOR
import urllib
from skimage import transform
from arcus.ml.images import conversion

_logger = logging.getLogger()

def load_image_from_disk(path: str, image_size:int = -1, 
                convert_to_grey: bool = False, keep_3d_shape = False) -> np.array:
    '''
    Loads an image from file, applying preformatting
    Args:
        path (str): The filename of the image to load
        image_size (int): If the image_size is larger than 0, the images will be resized to a square of this size
        convert_to_grey (bool): This would reduce the size (and shape) of the image in making it a greyscale
        keep_3d_shape (bool): Only used when convert_to_grey is true.  Will keep the images in shape (H,W,1) in that case
    Returns: 
        np.array: A numpy array that represents the image
    '''
    im = imread(path) 
    return conversion.prepare(im, image_size, convert_to_grey, keep_3d_shape)

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
        
        im = load_image_from_disk(os.path.join(path,f), image_size, convert_to_grey, keep_3d_shape)

        images.append(im)
        if(len(images) >= max_images and max_images > 0):
            break
    
    return np.array(images)

def load_image_from_url(image_url: str, image_size:int = -1, 
                convert_to_grey: bool = False, keep_3d_shape = False,
                cache_location: str = None, file_name: str = None, force_download: bool = False) -> np.array:
    '''
    Loads an image from a given url, applying preformatting and supporting file caching
    Args:
        image_url (str): The url to download the image.
        image_size (int): If the image_size is larger than 0, the images will be resized to a square of this size
        convert_to_grey (bool): This would reduce the size (and shape) of the image in making it a greyscale
        keep_3d_shape (bool): Only used when convert_to_grey is true.  Will keep the images in shape (H,W,1) in that case
        cache_location (str): When provided, the image will be cached to this folder location on disk
        file_name (str): The file name of the image to be cached
        force_download (bool): When true, the image will always be redownloaded and not retrieved from cache
    Returns: 
        np.array: A numpy array that represents the image
    '''
    image = []
    # If the users wants to cache, we first check if the image is 
    if (cache_location != None):
        import requests
        if not os.path.exists(cache_location):
            os.makedirs(cache_location)
        if not file_name:
            raise ValueError('Since caching was asked, a file_name attribute should be passed too')

        image_path = os.path.join(cache_location, file_name)

        if os.path.exists(image_path) and force_download == False:
            # We can return the cached image
            _logger.debug('We are taking the cached image from %s and will not download from %s', image_path, image_url)

        else:
            _logger.info('Downloading image from %s and saving to %s', image_url, image_path)
            urllib.request.urlretrieve(image_url, image_path)
        
        # Returning image that has been persisted anyhow
        return load_image_from_disk(image_path, image_size, convert_to_grey, keep_3d_shape)
        
    else:
        _logger.info('Downloading image from %s and return in memory', image_url)
        with urllib.request.urlopen(image_url) as url:
            s = url.read()
            print(type(s))
            image = np.asarray(bytearray(s), dtype="uint8")
            image = imdecode(image, IMREAD_COLOR)
            return conversion.prepare(image, image_size, convert_to_grey, keep_3d_shape)
