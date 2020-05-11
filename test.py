import time
import numpy as np

import ex_sum_py, ex_fib_py, ex_sort_py
import ex_sum_cy, ex_fib_cy, ex_sort_cy


def time_function(f, x):
    t = time.time()
    f(x)
    return time.time() - t


if __name__ == '__main__':
        
    t_py = time_function(ex_sum_py.get_sum, x=1_000_000)
    t_cy = time_function(ex_sum_cy.get_sum, x=1_000_000)
    print(f'ex_sum: t_py={t_py:.6f}, t_cy={t_cy:.6f}')

    t_py = time_function(ex_fib_py.get_series, x=10_000)
    t_cy = time_function(ex_fib_cy.get_series, x=10_000)
    print(f'ex_fib: t_py={t_py:.6f}, t_cy={t_cy:.6f}')

    array = np.random.randint(100, size=1_000)
    t_py = time_function(ex_sort_py.sort, x=array)
    t_cy = time_function(ex_sort_cy.sort, x=array)
    print(f'ex_sort: t_py={t_py:.6f}, t_cy={t_cy:.6f}')