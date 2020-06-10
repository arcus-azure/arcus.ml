import setuptools
import arcus.ml
import sys

from setuptools.command.test import test as TestCommand
from setuptools import find_namespace_packages

with open("package-description.md", "r") as fh:
    long_description = fh.read()

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

packages_to_import = setuptools.find_packages(exclude=['tests', 'docs', 'build', 'samples'])

print('Package to import:')
print(packages_to_import)
print('=============')

setuptools.setup(
    name="arcus-ml", 
    version=arcus.ml.__version__,
    author="Arcus",
    author_email="arcus-automation@codit.eu",
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    description="A Python library that provides best practices for Python Machine Learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arcus-azure/arcus.ml",
    packages=find_namespace_packages(include=['arcus.*'], exclude=['tests', 'docs', 'build', 'samples']),
    package_dir={'arcus.ml': 'arcus/ml'},
    namespace_packages=['arcus'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    extras_require={
        'testing': ['pytest'],
    }
)
