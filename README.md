# Arcus - Machine Learning
[![Build Status](https://dev.azure.com/codit/Arcus/_apis/build/status/arcus-azure.arcus.ml?branchName=master)](https://dev.azure.com/codit/Arcus/_build/latest?definitionId=836&branchName=master) [![PyPI version](https://badge.fury.io/py/arcus-ml.svg)](https://badge.fury.io/py/arcus-ml)

Python Machine Learning development in a breeze.

![Arcus](https://raw.githubusercontent.com/arcus-azure/arcus/master/media/arcus.png)

# Positioning

With Arcus we are offering an open source library that streamlines ML development with Python and offers out of the box implementations for common scenarios.


# Features

Coming soon

# Installation

The Arcus packages are available through PyPi and can be installed through pip, by executing the following command:

```shell
PM > pip3 install arcus-ml
```

Upgrading to the latest version can be done by executing the following pip command:

```shell
PM > pip3 install --upgrade arcus-ml 
```

Every CI build pushes a dev package to the PyPi feed.  And when committed, an alpha release is been published on the same feed.  These packages can be installed or up  grade, by leveraging the `--pre` argument for `pip`.

```shell
PM > pip3 install --upgrade --pre arcus-ml
```

# Local development
    
It can be quite common that you are using the arcus-ml or arcus-azureml packages on other projects and you need some changes or additional functionality being added to the package.  Obviously, it's possible to follow the entire release pipeline (make a PR, get it approved and merged, wait for package to appear on the PyPi feed and upgrade the package).  This workflow is too tedious and will not increase your productivity.

The approach to go, is to leverage the following command, which will add a symbolic link to your development directory from the python packages.  That way, you always refer to the latest code that is on your development environment.  It is advised, though not required to leverage virtual environment (like with conda) for this.

```shell
pip install -e /path-to-arcus
```

## Code documentation

The modules and methods have to be documented and decorated with Google Style Python Docstrings.  These docstrings will be used by `lazydocs` to automatically generate the SDK documentation for the Arcus library.

# Build process

The actual build process executes the following steps:

1. Update package version, based on build
2. Install following python packages: `pip`, `setuptools`, `wheel`, `pdoc3` and `lazydocs`
3. Install the prerequisites from the `requirements.txt` file
4. Run the unit tests, found in the solution
5. Publish the test & code coverage results
6. Build & push the packages (wheels)
7. Generate the code documentation, using lazydocs

# Customers
Are you an Arcus user? Let us know and [get listed](https://bit.ly/become-a-listed-arcus-user)!

# License Information
This is licensed under The MIT License (MIT). Which means that you can use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the web application. But you always need to state that Codit is the original author of this web application.
