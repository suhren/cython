# Cython

Cython code is annotated "Python-like" code which is compiled to `C` or `C++`. This is then wrapped in "interface code" which prodcuces "extension modules" that can be used directly in Python. 

The `C` or `C++` code use static types and offer lower overhead in control structures and function calls which can in turn greatly speed up performance on native python code.

# Installation
More detailed descriptions of the installation can be found [here](https://cython.readthedocs.io/en/latest/src/quickstart/install.html). In short, the latest Cython release can easily be installed with the command
```
pip install cython
```

## C Compiler Installation
Cython also requires a `c` compiler to be present on the system. This installation will differ depending on what operatin system you are using. 

### Linux Installation
The GNU C Compiler (`gcc`) should be available by default in e.g. Ubuntu. If not, it can be installed using
```
sudo apt-get install build-essential
``` 

### Windows Installation
`gcc` is not available on Windows by default. Instead we can use `MinGW` which includes a port of the GNU Compiler Collection (GCC), including C, C++, ADA and Fortran compilers.

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
If you want to learn more about the basics of `Cython`, you can have a look at [this tutorial](https://pythonprogramming.net/introduction-and-basics-cython-tutorial/).

A few important keywords to keep in mind are:
* `def` - Ordinary Python functions which can only be called from Python
* `cdef` - Pure Cython functions which can only be called from Cython
* `cpdef`- C function with a Python wrapper

This repository includes three different example programs with the `.py` extension for ordinary python modules and `.pyx` for code that will be used by Cython to compile to `C` code.

To compile the code, we run the following command:
```
python setup.py build_ext --inplace
```

After the build has finished, we can run `test.py` to see how the execution time of the native python code compares with the compiled `Cython` code. In many cases it can over a hundred times faster!
```
python test.py
```