from libcpp.vector cimport vector

def min_multiply():
    cdef list prime_array = [2, 3, 5, 7, 11, 13, 17, 19]
    cdef int result = 1
    cdef int prime
    cdef int p
    for prime in prime_array:
        p = prime
        while p * prime < 20:
            p *= prime
        result *= p
    return result


def min_multiply_v3():
    cdef vector[int] prime_array = [2, 3, 5, 7, 11, 13, 17, 19]
    cdef int result = 1
    cdef int prime
    cdef int p
    for prime in prime_array:
        p = prime
        while p * prime < 20:
            p *= prime
        result *= p
    return result