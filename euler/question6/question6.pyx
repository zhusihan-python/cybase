def difference():
    cdef int i 
    cdef int sum = 0
    cdef int pow_sum = 0
    cdef int sum_pow = 0
    for i in range(1, 101):
        sum += i
        sum_pow += i * i
    pow_sum = sum * sum
    return  pow_sum - sum_pow
