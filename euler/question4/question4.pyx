from cython cimport boundscheck, wraparound
from cython.parallel import prange


cdef is_palindromic(n):
    cdef str n_str = str(n)
    return n_str == n_str[::-1]


cdef is_palindromic_v2(int n):
    cdef int original_n = n
    cdef int reversed_n = 0
    cdef int rem
    while n > 0:
        rem = n % 10
        reversed_n = reversed_n * 10 + rem
        n /= 10
    return original_n == reversed_n


cdef int is_palindromic_v3(int n) nogil:
    cdef int original_n = n
    cdef int reversed_n = 0
    cdef int rem
    while n > 0:
        rem = n % 10
        reversed_n = reversed_n * 10 + rem
        n /= 10
    return original_n == reversed_n


def is_palindromic_v3_wrap(n):
    return is_palindromic_v3(n)


@boundscheck(False)
@wraparound(False)
def max_palindromic():
    cdef int max_palindromic = 0
    cdef int i, j, prod
    for i in range(100, 1000):
        for j in range(100, 1000):
            prod = i * j
            if is_palindromic(prod) and prod > max_palindromic:
                max_palindromic = prod
    return max_palindromic


@boundscheck(False)
@wraparound(False)
def max_palindromic_v2():
    cdef int max_palindromic = 0
    cdef int i, j, prod
    for i in range(100, 1000):
        for j in range(100, 1000):
            prod = i * j
            if is_palindromic_v2(prod) and prod > max_palindromic:
                max_palindromic = prod
    return max_palindromic


# https://mail.python.org/pipermail/cython-devel/2011-July/001139.html
# https://github.com/cython/cython/issues/5494
@boundscheck(False)
@wraparound(False)
def max_palindromic_v3():
    cdef int i, j
    cdef int max_palindromic = 0
    cdef int prod = 0
    for i in prange(100, 101, nogil=True):
        for j in range(100, 101):
            prod = i * j
            if is_palindromic_v3(prod) == 1 and prod > max_palindromic:
                max_palindromic = prod
    return max_palindromic
