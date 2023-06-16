def fib(n):
    cdef int i
    cdef int a = 0, b = 1
    while a <= n:
        yield a
        a, b = b, a + b


def even_fibonacci_sum(n):
    cdef int total = 0
    for num in fib(n):
        if num % 2 == 0:
            total += num
    return total


def even_fibonacci_sum_v2(int n):
    cdef int a = 0, b = 1, total = 0
    while a <= n:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return total
