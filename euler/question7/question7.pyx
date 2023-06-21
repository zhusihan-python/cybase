from libc.math cimport sqrt, log
from libcpp.vector cimport vector
from libcpp cimport bool

cdef int is_prime(number):
    cdef int end
    if number == 2:
        return 1
    elif number % 2 == 0:
        return 0
    else:
        end = <int>sqrt(number) + 1
        for i in range(3, end, 2):
            if number % i == 0:
                return 0
    return 1


def prime_number():
    cdef int n = 3
    cdef int i = 2
    while i < 10002:
        if is_prime(n) == 1:
            i += 1
        n += 2
    return n - 2


def primes_sieve_list(n):
    cdef int p_n = int(2 * n * log(n))
    cdef list[bool] sieve = [True] * p_n
    cdef int count = 0
    for i in range(2, p_n):
        if sieve[i]:
            count += 1
            if count == n:
                return i
            for j in range(2*i, p_n, i):
                sieve[j] = False


def primes_sieve_vector(n):
    cdef int p_n = int(2 * n * log(n))
    # cdef list[bool] sieve = [True] * p_n
    cdef vector[bool] sieve
    cdef int count = 0
    for i in range(p_n):
        sieve.push_back(True)
    for i in range(2, p_n):
        if sieve[i]:
            count += 1
            if count == n:
                return i
            for j in range(2*i, p_n, i):
                sieve[j] = False
