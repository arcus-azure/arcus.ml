import sys
import os
import pytest
import pandas as pd 
import arcus.ml.images.io as ami
import arcus.ml.images.conversion as conv
import logging
import numpy as np 

image_path = 'tests/resources/images/lungs'

def test_black_white_conversion():
    image_list = ami.load_images(image_path)
    ls = conv.to_blackwhite(image_list)
    pixel_value = ls[0][0][0]
    assert pixel_value == 0 or pixel_value == 1
    assert len(ls[0].shape)==2

def test_black_white_conversion_double_arrays():
    image_list = ami.load_images(image_path)
    test_list = list()
    for img in image_list:
        test_list.append(img / 255)
    ls = conv.to_blackwhite(np.array(test_list))
    pixel_value = ls[0][0][0]
    assert pixel_value == 0 or pixel_value == 1

def test_crop_image():
    image = ami.load_images(image_path, max_images=1, image_size=50)[0]
    crop = conv.crop(image, 10, 20, 20, 10)
    assert crop.shape == (10, 20, 3)

def test_black_white_conversion_3dshape():
    image_list = ami.load_images(image_path)
    ls = conv.to_blackwhite(image_list, keep_3d_shape=True)
    pixel_value = ls[0][0][0]
    assert pixel_value == 0 or pixel_value == 1
    assert len(ls[0].shape)==3

def test_black_white_conversion_2x3dshape():
    lung = ami.load_images(image_path, convert_to_grey=True, image_size = 30, keep_3d_shape=True)[0]
    assert lung.shape == (30, 30, 1)
    lung = conv.to_blackwhite([lung], keep_3d_shape=True, threshold=200)
    assert lung[0].shape == (30, 30, 1)