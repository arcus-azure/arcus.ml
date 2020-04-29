import sys
import os
import pytest
import pandas as pd 
import arcus.ml.images.io as ami
import logging

image_path = 'tests/resources/images/lungs'

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