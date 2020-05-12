'''
The io module provides standard helper functions to load images from disk
'''

import logging
import os
import numpy as np
from cv2 import imread, imdecode, IMREAD_COLOR
import requests
from skimage import transform
from arcus.ml.images import conversion
from arcus.ml import dataframes as adf
from io import BytesIO
import pandas as pd

_logger = logging.getLogger()

def load_image_from_disk(path: str, image_size = None, 
                convert_to_grey: bool = False, keep_3d_shape = False) -> np.array:
    '''
    Loads an image from file, applying preformatting
    Args:
        path (str): The filename of the image to load
        image_size (tuple): The image size can be passed as tuple (W, H) or as int (W=H)
        convert_to_grey (bool): This would reduce the size (and shape) of the image in making it a greyscale
        keep_3d_shape (bool): Only used when convert_to_grey is true.  Will keep the images in shape (H,W,1) in that case
    Returns: 
        np.array: A numpy array that represents the image
    '''
    im = imread(path) 
    return conversion.prepare(im, image_size, convert_to_grey, keep_3d_shape)

def load_images(path: str, image_size = None, max_images: int = -1, 
                valid_extensions: np.array = ['.jpg','.jpeg','.gif','.png'],
                convert_to_grey: bool = False, keep_3d_shape = False) -> np.array:
    '''
    Loads the images from a specific folder
    Args:
        path (str): The path or folder name to load images from.  This can be a relative or fully qualified path
        image_size (tuple): The image size can be passed as tuple (W, H) or as int (W=H)
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

def load_image_from_url(image_url: str, http_headers: dict = None, image_size = None, 
                convert_to_grey: bool = False, keep_3d_shape = False,
                cache_location: str = None, file_name: str = None, force_download: bool = False) -> np.array:
    '''
    Loads an image from a given url, applying preformatting and supporting file caching
    Args:
        image_url (str): The url to download the image.
        http_headers (dict): The http headers to pass with the request as a dictionary
        image_size (tuple): The image size can be passed as tuple (W, H) or as int (W=H)
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
            with requests.get(image_url, headers = http_headers, stream=True) as _http_response:
                if(str(_http_response.status_code).startswith('2')):
                    with open(image_path, 'wb') as fd:
                        for chunk in _http_response.iter_content(chunk_size=128):
                            fd.write(chunk)
                else:
                    raise Exception('HTTP error: ' + str(_http_response.status_code))
        # Returning image that has been persisted anyhow
        return load_image_from_disk(image_path, image_size, convert_to_grey, keep_3d_shape)
        
    else:
        _logger.info('Downloading image from %s and return in memory', image_url)
        with requests.get(image_url, headers = http_headers) as _http_response:
            if(str(_http_response.status_code).startswith('2')):
                image = np.asarray(bytearray(_http_response.content), dtype="uint8")
                image = imdecode(image, IMREAD_COLOR)
                return conversion.prepare(image, image_size, convert_to_grey, keep_3d_shape)
            else:
                raise Exception('HTTP error: ' + str(_http_response.status_code))

def load_images_from_dataframe(df: pd.DataFrame, image_column_name:str, target_column_name: str, 
                                image_size = None, max_images: int = -1, target_as_image: bool = False,
                                convert_to_grey: bool = False, keep_3d_shape = False) -> (np.array, np.array):
    '''
    Loads the images from a specific folder
    Args:
        path (str): The path or folder name to load images from.  This can be a relative or fully qualified path
        image_size (tuple): The image size can be passed as tuple (W, H) or as int (W=H)
        max_images (int): The maximum amount of images to load from the folder.  If 0 or smaller, all images will be returned
        target_as_image (bool): Defines if the target column contains file names that should be loaded as image
        valid_extensions (np.array): The file extensions that should be filtered.  Defaults to jpg, jpeg, gif and png
        convert_to_grey (bool): This would reduce the size (and shape) of the image in making it a greyscale
        keep_3d_shape (bool): Only used when convert_to_grey is true.  Will keep the images in shape (H,W,1) in that case
    Returns: 
        np.array: A numpy array that contains all selected images represented as np.array
    '''
    images = []
    targets = []
    df = adf.shuffle(df)
    for idx, row in df.iterrows() :
        file = row[image_column_name]
        if file and os.path.exists(file):
            if target_as_image:
                # Check if the target file exists
                target_file = row[target_column_name]
                if target_file and os.path.exists(target_file):
                    im = load_image_from_disk(file, image_size, convert_to_grey, keep_3d_shape)
                    target_im = load_image_from_disk(target_file, image_size, convert_to_grey, keep_3d_shape)
                    images.append(im)
                    targets.append(target_im)
                else:
                    _logger.warning('File ' + target_file + ' not found')
            else:
                im = load_image_from_disk(file, image_size, convert_to_grey, keep_3d_shape)
                images.append(im)
                targets.append(row[target_column_name])
        else:
            _logger.warning('File ' + file + ' not found')

        if(len(images) >= max_images and max_images > 0):
            break
    
    return np.array(images), np.array(targets)