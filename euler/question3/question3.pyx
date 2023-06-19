def max_prime_factor(number):
    cdef long long n = number
    if n <= 1:
        return 0
    cdef long long num = 0
    cdef long long i
    for i in range(2, n):
        if i * i > n:
            break
        while n % i == 0:
            num = i
            n = n // i
    if n > 1:
        num = n
    return num
