import numpy as np
cimport numpy as np
cimport cython

cpdef np.ndarray[np.int32_t, ndim=1] get_series(int n):
    cdef int a = 0
    cdef int b = 1
    cpdef np.ndarray[np.int32_t, ndim=1] result = np.zeros((n), dtype=np.int32)
    cdef int i
    cdef int temp

    for i in range(n):
        temp = a
        a = b
        b = temp + b
        result[i] = a

    return result