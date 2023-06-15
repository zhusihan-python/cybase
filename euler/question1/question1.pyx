from cython.parallel import prange
from cython cimport boundscheck, wraparound


@boundscheck(False)
@wraparound(False)
def get_sum_multiples():
    cdef short total = 0
    cdef short start = 1
    cdef short end = 1000
    cdef short i
    for i in prange(start, end, nogil=True):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


# range performance better than prange 4-5 times
@boundscheck(False)
@wraparound(False)
def get_sum_multiples_gil():
    cdef short total = 0
    cdef short start = 1
    cdef short end = 1000
    cdef short i
    for i in range(start, end):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total
