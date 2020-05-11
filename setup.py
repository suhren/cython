import numpy
from distutils.core import setup
from Cython.Build import cythonize

# Use numpy.get_include() to locate the numpy source files location

setup(
    ext_modules=cythonize([
        'ex_sum_cy.pyx',
        'ex_fib_cy.pyx',
        'ex_sort_cy.pyx'
    ]),
    include_dirs=[
        numpy.get_include()
    ]
)