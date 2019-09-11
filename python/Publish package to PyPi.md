
# Python packages and modules

## Creating and using a module

A Python module is simple a separate Python file containing code you wish to import into your main program.

If you have a file called `module1.py` in the same folder as your existing project.

```python
import module1

module1.cool_function()
```

Or

```python
from module1 import cool_function

cool_function()
```

## Creating and using a package of modules

A **package of modules** in Python consists of creating a folder to contain the files, where the folder name becomes the package name, and the Python filenames become your module names.

The only catch is the folder **must** contain a file called `__init__.py`. The file can be empty, but it must exist.

So, with the following folder & file structure:

```
packageA/
  __init__.py        <-- empty file but must exist
  module1.py
  module2.py
```

In your application, you would import items as follows

```python
import packageA.module1

packageA.module1.cool_function()
```

Or

```python
from packageA import module1
module1.cool_function()
```

Or

```python
from packageA.module1 import cool_function
cool_function()
```

## Publishing a package on PyPi

Want to share your amazing package with the rest of the Python world so they can install it with PIP? It's quite easy to do!

### Step 1 - Create your package

As detailed above

### Step 2 - Put your package into the following folder structure

Folder structure of sharable package

```txt
containing_folder/
   package/
      __init__.py
      module1.py
      module2.py
   LICENSE.TXT
   README.MD
   setup.cfg
   setup.py
```

Edit your `package/__init__.py` file to contain a name variable

```python
name = "example_pkg"
```

### Step 3 - Build your PyPi required files

LICENSE.TXT example

```txt
MIT License

Copyright (c) 2018 Paul Baumgarten

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

setup.cfg example

```txt
[metadata]
license_file = LICENSE.txt

[bdist_wheel]
# 1 = code supports Python 2 and 3
# 0 = not universial, Python 2 OR Python 3
# https://packaging.python.org/guides/distributing-packages-using-setuptools/#wheels
universal=0
```

setup.py example

```python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easyaspi",
    version="2018.3",
    author="Paul Baumgarten",
    author_email="pbaumgarten@gmail.com",
    description="A module intended to abstract away a lot of the complexity of using the GPIO and PiCamera for beginner programmers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/easyaspi",
    packages=setuptools.find_packages(),
    keywords='raspberrypi GPIO picamera beginner',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['rpi.gpio','picamera'],
    python_requires='>=3'
)
```

Refer to [https://packaging.python.org/tutorials/packaging-projects/](https://packaging.python.org/tutorials/packaging-projects/) for the options of the setup() function.

### Step 4 - Generate distribution files

Install setuptools and wheel if you don't already have them

```bash
python3 -m pip install --user --upgrade setuptools wheel
```

Run this command in the folder that contains setup.py

```bash
python3 setup.py sdist bdist_wheel
```

This will create a `dist/` folder with two files

```txt
dist/
  example_pkg-0.0.1-py3-none-any.whl
  example_pkg-0.0.1.tar.gz
```

### Step 5 - Upload to PyPi

Sign up to PyPi for an account if you don't have one

* [https://pypi.org/account/register/](https://pypi.org/account/register/)

Install Twine if you haven't previously done so

```bash
python3 -m pip install --user --upgrade twine
```

Use Twine to upload to PyPi

```bash
python3 -m twine upload dist/*
```

Congratulations, your package should now be available for the world to install via pip

```bash
pip install [your-package]
```