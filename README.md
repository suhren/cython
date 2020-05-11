# Cython Exploration

## Cython Installation

```
pip install cython
```


## C Compiler Installation

### Linux Installation
The GNU C Compiler (gcc) should be available by default in e.g. Ubuntu. If not, it can be installed using
```
sudo apt-get install build-essential
``` 

## Windows Installation
https://cython.readthedocs.io/en/latest/src/quickstart/install.html
https://superuser.com/questions/1479075/installing-anaconda-on-git-bash-and-trying-conda-activate-results-in-repeated-co

### Install MinGW

1. Install MinGW from [here](http://www.mingw.org/wiki/HOWTO_Install_the_MinGW_GCC_Compiler_Suite)
1. Run the installer. Only the basic package is needed for Cython, but the C++ compiler might be useful as well.
1. Add the installation `bin` directory to the Windows PATH variable, e.g. `c:\mingw\bin`.
1. Specify `mingw32` as the default compiler of your python installation by creating a file called `distutils.cfg` with the following information:
        
        [build]
        compiler = mingw32

    * E.g. default location of the python interpreter:
        * `C:\Users\<user>\AppData\Local\Programs\Python\<version>\Lib\distutils\distutils.cfg`
    * E.g. Anaconda environment named `cython`:
        * `C:\Users\<user>\Anaconda3\envs\cython\Lib\distutils\distutils.cfg`


# Usage
https://pythonprogramming.net/introduction-and-basics-cython-tutorial/

* `def` - Ordinary Python functions which can only be called from Python
* `cdef` - Pure Cython functions which can only be called from Cython
* `cpdef`- C function with a Python wrapper


```
#setup.py

from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('example_cy.pyx'))
```


```
#setup.py

from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('example_cy.pyx'))
```


```
python setup.py build_ext --inplace
```

Use `numpy.get_include()` to locate the numpy source files location