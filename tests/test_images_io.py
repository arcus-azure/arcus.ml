import sys
import os
import pytest
import pandas as pd 
import arcus.ml.images.io as ami
import logging
import shutil

image_path = 'tests/resources/images/lungs'
image_url = 'https://cdn.sstatic.net/Sites/stackoverflow/img/apple-touch-icon@2.png'
image_url2 = 'https://github.com/arcus-azure/arcus/raw/master/media/arcus.png'
cache_directory = 'tests/resources/temp/io'
cache_file_name = 'testimage.png'

def setup_module(module):
    ''' Setup for the entire module '''
    # Do the actual setup stuff here
    pass

def setup_function(func):
    ''' Setup for test functions '''
    # cache_directory = os.path.join(os.getcwd(), 'tests/resources/temp/io')
    if os.path.exists(cache_directory):
        shutil.rmtree(cache_directory)
    os.mkdir(cache_directory)

def test_load_single_image():
    image_file_name = 'tests/resources/images/lungs/CHNCXR_0001_0.png'
    image = ami.load_image_from_disk(image_file_name, image_size=40)

    assert(image.shape == (40, 40, 3))

def test_load_images_defaults():
    image_list = ami.load_images(image_path)

    assert len(image_list) == 11

def test_load_images_max_number():
    image_list = ami.load_images(image_path, max_images=4)

    assert len(image_list) == 4

def test_load_images_resize():
    image_list = ami.load_images(image_path, image_size=40, max_images=1)

    assert len(image_list) == 1
    assert image_list[0].shape == (40, 40, 3)

def test_load_images_grey():
    image_list = ami.load_images(image_path, image_size=40, max_images=1, convert_to_grey=True)

    assert image_list[0].shape == (40, 40)
    assert len(image_list) == 1

def test_load_images_grey_keep_shape():
    image_list = ami.load_images(image_path, image_size=40, max_images=1, convert_to_grey=True, keep_3d_shape=True)

    assert image_list[0].shape == (40, 40, 1)
    assert len(image_list) == 1

def test_load_images_grey_dont_keep_shape():
    image_list = ami.load_images(image_path, image_size=40, max_images=1, convert_to_grey=True, keep_3d_shape=False)

    assert image_list[0].shape == (40, 40)
    assert len(image_list) == 1

def test_load_images_extensions():
    image_list = ami.load_images(image_path, valid_extensions=['.gif'])

    assert len(image_list) == 0

def test_image_url_to_memory():
    image = ami.load_image_from_url(image_url)
    assert len(image.shape) == 3

def test_image_url_to_cache():
    cached_file_name = os.path.join(cache_directory, cache_file_name)
    assert os.path.exists(cached_file_name)==False
    image = ami.load_image_from_url(image_url, cache_location=cache_directory, file_name=cache_file_name, force_download=False)
    assert len(image.shape) == 3
    assert os.path.exists(cached_file_name)
    disk_image = ami.load_image_from_disk(cached_file_name)
    assert disk_image.shape == image.shape

def test_image_url_through_cache():
    cached_file_name = os.path.join(cache_directory, cache_file_name)
    assert os.path.exists(cached_file_name)==False
    # Force download of 1st image
    image = ami.load_image_from_url(image_url, cache_location=cache_directory, file_name=cache_file_name, force_download=True)
    assert len(image.shape) == 3
    assert os.path.exists(cached_file_name)

    # Cached download of 2nd image
    image2 = ami.load_image_from_url(image_url2, cache_location=cache_directory, file_name=cache_file_name)
    assert len(image.shape) == 3
    assert os.path.exists(cached_file_name)
    # Even tough url was different, the image should be the same
    assert image.shape == image2.shape

def test_image_url_through_cache_missingfile():
    # Trigger missing 
    with pytest.raises(ValueError) as val_err:
        ami.load_image_from_url(image_url, cache_location=cache_directory, file_name='')
    assert 'file_name' in str(val_err.value)

def test_image_url_unauthorized():
    # Trigger missing 
    with pytest.raises(Exception) as val_err:
        ami.load_image_from_url('https://stockcharts.com/c-sc/sc?s=AAPL&p=W&yr=3&mn=0&dy=0&i=t5753201539c&r=1588670112897')
    assert '403' in str(val_err.value)

def test_image_url_headers():
    # Trigger missing 
    img = ami.load_image_from_url('https://stockcharts.com/c-sc/sc?s=AAPL&p=W&yr=3&mn=0&dy=0&i=t5753201539c&r=1588670112897',
        http_headers={'User-Agent': 'Postman'})
    assert len(img.shape) == 3
