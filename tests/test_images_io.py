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
    for filename in os.listdir(cache_directory):
        if (filename != '__emptyfile__'):     
            file_path = os.path.join(cache_directory, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                #elif os.path.isdir(file_path):
                #    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
    # cache_directory = os.path.join(os.getcwd(), 'tests/resources/temp/io')
    #if os.path.exists(cache_directory):
    #    shutil.rmtree(cache_directory)
    #os.mkdir(cache_directory)
    #os.chdir(cache_directory)
    #os.mkdir(cache_directory)

def test_load_single_image():
    image_file_name = 'tests/resources/images/lungs/CHNCXR_0001_0.png'
    image = ami.load_image_from_disk(image_file_name, image_size=40)

    assert(image.shape == (40, 40, 3))

def test_load_single_image_notexist():
    image_file_name = 'tests/resources/images/lungs/missingfile.png'
    with pytest.raises(FileNotFoundError) as fnf_err:
        image = ami.load_image_from_disk(image_file_name, image_size=40)
    assert image_file_name in str(fnf_err)

def test_load_images_defaults():
    image_list = ami.load_images(image_path)

    assert len(image_list) == 11

def test_load_images_max_number():
    image_list = ami.load_images(image_path, max_images=4)

    assert len(image_list) == 4

def test_load_images_resize_square():
    image_list = ami.load_images(image_path, image_size=40, max_images=1)

    assert len(image_list) == 1
    assert image_list[0].shape == (40, 40, 3)

def test_load_images_resize_tuple():
    image_list = ami.load_images(image_path, image_size=(40, 30), max_images=1)

    assert len(image_list) == 1
    assert image_list[0].shape == (40, 30, 3)

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


def test_image_url_resize_memory():
    img_path = 'https://charting.vwdservices.com/tchart/tchart.aspx?user=Tijdnet&issue=360017012&layout=gradient-v1&startdate=3Y&enddate=today&res=endofday&width=876&height=400&format=image/png&culture=nl-BE'
    image = ami.load_image_from_url(img_path)
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

def test_load_images_df_multi():
    df = pd.read_csv('tests/resources/datasets/lung-files.csv')
    X, outputs = ami.load_images_from_dataframe(df, 'lungfile', ['result','maskfile'])
    assert len(X) == 11
    output1 = outputs[0]
    assert output1[0] in ('0', '1')
    assert os.path.exists(output1[1])

def test_load_images_set_df():
    df = pd.read_csv('tests/resources/datasets/lung-files.csv')
    X, y = ami.load_images_from_dataframe(df, 'lungfile', 'maskfile', target_as_image=True)
    assert len(X) == 11
    assert len(y[0].shape) == 3

def test_load_images_df():
    df = pd.read_csv('tests/resources/datasets/lung-files.csv')
    X, y = ami.load_images_from_dataframe(df, 'lungfile', 'result')
    assert len(X) == 11
    assert y[3] in (0, 1)

def test_load_images_df_sourcemissing():
    df = pd.read_csv('tests/resources/datasets/lung-files-missing-files.csv')
    # Two records contain a non existing file.  
    # 1 with source missing: output = 2
    # Another with destination missing: output = 0
    X, y = ami.load_images_from_dataframe(df, 'lungfile', 'result')
    assert len(X) == 10
    assert y[3] in (0, 1)

    assert 0 in y
    assert 1 in y
    assert not 2 in y

def test_load_images_df_destmissing():
    df = pd.read_csv('tests/resources/datasets/lung-files-missing-files.csv')
    # Two records contain a non existing file.  
    # 1 with source missing: output = 2
    # Another with destination missing: output = 0
    X, y = ami.load_images_from_dataframe(df, 'lungfile', 'maskfile', target_as_image=True)
    assert len(X) == 9
