import setuptools 

def test_package_discovery():
    assert len(setuptools.find_packages('arcus')) > 0
    assert len(setuptools.find_packages('tests')) == 0
    assert len(setuptools.find_packages('samples')) == 0
