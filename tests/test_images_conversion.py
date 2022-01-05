import sys
import os
import pytest
import pandas as pd 
import arcus.ml.images.io as ami
import arcus.ml.images.conversion as conv
import logging
import numpy as np
from hypothesis import given, event, settings, note, Verbosity, strategies as st

image_path = 'tests/resources/images/lungs'

def is_black_or_white(cell):
    return cell == 0 or cell == 1
def all_black_and_white(arr):
    result = []
    for cell_z in arr:
        for cell_y in cell_z:
            if isinstance(cell_y, np.ndarray):
                for cell_x in cell_y:
                    result.append(is_black_or_white(cell_x))
            else:
                result.append(is_black_or_white(cell_y))
    return all(result)

@st.composite
def images(draw, dimension = 3):
    def create_array_rec(strategy, lengths, index = 0):
        if index == len(lengths):
            return strategy
        length = lengths[index]
        arr = st.lists(strategy, min_size=length, max_size=length).map(lambda x : np.array(x))
        return create_array_rec(arr, lengths, index + 1)

    num = st.integers(min_value=0, max_value=255)
    amount = st.integers(min_value=1, max_value=10)
    return draw(st.lists(amount, min_size=dimension, max_size=dimension).flatmap(lambda lengths : create_array_rec(num, lengths)))

@given(images())
def test_black_white_property(image_list):
    image_converted = conv.to_blackwhite(image_list)
    assert all_black_and_white(image_converted)

@given(images(dimension=2))
def test_black_white_2D_property(image_list):
    image_converted = conv.to_blackwhite(image_list)
    assert all_black_and_white(image_converted)

def test_black_white_empty_stays_empty():
    image_converted = conv.to_blackwhite(np.array([]))
    image_converted = []

@given(images(), st.integers().filter(lambda x : x < 0 or x > 255))
def test_black_white_outofbounds_threshold(image_list, threshold):
    with pytest.raises(ValueError, match=r".* threshold .*"):
        conv.to_blackwhite(image_list, threshold)

def test_black_white_conversion():
    image_list = ami.load_images(image_path)
    image_converted = conv.to_blackwhite(image_list)
    assert all_black_and_white(image_converted)

def test_black_white_conversion_double_arrays():
    image_list = ami.load_images(image_path)
    test_list = image_list / 255
    image_converted = conv.to_blackwhite(np.array(test_list))
    assert all_black_and_white(image_converted)

def test_crop_image():
    image = ami.load_images(image_path, max_images=1, image_size=50)[0]
    crop = conv.crop(image, 10, 20, 20, 10)
    assert crop.shape == (10, 20, 3)

def test_black_white_conversion_3dshape():
    image_list = ami.load_images(image_path)
    image_converted = conv.to_blackwhite(image_list, keep_3d_shape=True)
    assert all_black_and_white(image_converted)

def test_black_white_conversion_2x3dshape():
    lung = ami.load_images(image_path, convert_to_grey=True, image_size = 30, keep_3d_shape=True)[0]
    assert lung.shape == (30, 30, 1)
    lung = conv.to_blackwhite([lung], keep_3d_shape=True, threshold=200)
    assert lung[0].shape == (30, 30, 1)