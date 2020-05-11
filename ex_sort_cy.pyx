import numpy as np
cimport numpy as np
cimport cython

cpdef np.ndarray[np.int32_t, ndim=1] sort(np.ndarray[np.int32_t, ndim=1] array):

    cdef int n = len(array)
    cpdef np.ndarray[np.int32_t, ndim=1] x = array.copy()
    cdef int i = 0
    cdef int j = 0
    cdef int temp

    for i in range(n):
        for j in range(i, n):
            if x[i] > x[j]:
                temp = x[i]
                x[i] = x[j]
                x[j] = temp

    return x