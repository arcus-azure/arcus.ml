import sys
import os
import pytest
import pandas as pd 
import arcus.ml.images.explorer as exp
import arcus.ml.images.io as imgio
import arcus.ml.images.conversion as conv
import logging

image_path_1 = 'tests/resources/images/lungs'
image_path_2 = 'tests/resources/images/lungmasks'

def test_visualize_random_images():
    lungs = imgio.load_images(image_path_1)
    masks = imgio.load_images(image_path_2)

    exp.visualize({'lungs': lungs, 'masks': masks}, image_count = 6, randomize=True)

def test_visualize_first_images():
    lungs = imgio.load_images(image_path_1)
    masks = imgio.load_images(image_path_2)

    exp.visualize({'lungs': lungs, 'masks': masks}, image_count = 6, randomize=False)

def test_visualize_3d_shape_images():
    lungs = imgio.load_images(image_path_1, convert_to_grey=True, keep_3d_shape=True)
    masks = imgio.load_images(image_path_2, convert_to_grey=True, keep_3d_shape=True)

    exp.visualize({'lungs': lungs, 'masks': masks}, image_count = 6, randomize=True)


def test_visualize_oneset_images():
    lungs = imgio.load_images(image_path_1)

    exp.visualize({'lungs': lungs}, image_count = 6, randomize=True)

def test_show_3d_shape_image():
    lungs = imgio.load_images(image_path_1, convert_to_grey=True, keep_3d_shape=True)
#X = conversion.to_blackwhite(X, keep_3d_shape=True, threshold=200)
    exp.show_image(lungs[1])

def test_visualize_random_images_silent():
    lungs = imgio.load_images(image_path_1)
    masks = imgio.load_images(image_path_2)

    pp = exp.visualize({'lungs': lungs, 'masks': masks}, image_count = 6, randomize=True, silent_mode=True)
    assert pp is not None

def test_visualize_first_images_silent():
    lungs = imgio.load_images(image_path_1)
    masks = imgio.load_images(image_path_2)

    pp = exp.visualize({'lungs': lungs, 'masks': masks}, image_count = 6, randomize=False, silent_mode=True)
    assert pp is not None

def test_visualize_3d_shape_images_silent():
    lungs = imgio.load_images(image_path_1, convert_to_grey=True, keep_3d_shape=True)
    masks = imgio.load_images(image_path_2, convert_to_grey=True, keep_3d_shape=True)

    pp = exp.visualize({'lungs': lungs, 'masks': masks}, image_count = 6, randomize=True, silent_mode=True)
    assert pp is not None


def test_visualize_oneset_images_silent():
    lungs = imgio.load_images(image_path_1)

    pp = exp.visualize({'lungs': lungs}, image_count = 6, randomize=True, silent_mode=True)
    assert pp is not None

def test_show_3d_shape_image_silent():
    lungs = imgio.load_images(image_path_1, convert_to_grey=True, keep_3d_shape=True)

    pp = exp.show_image(lungs[1], silent_mode=True)
    assert pp is not None

