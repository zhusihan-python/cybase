from libcpp.vector cimport vector
from libcpp.algorithm cimport max_element
from libc.string cimport strlen
# from libc.stdio cimport printf
from cython.operator cimport dereference as deref

def max_multiply():
    cdef int i
    cdef long long prod
    cdef list sub
    with open('ep08.txt', 'r') as f:
        data = ''
        for line in f.readlines():
            data = data + line.strip()
    cdef vector[long long] res

    for i in range(988):
        sub = [ <long long>int(data[i+j]) for j in range(13) ]
        prod = 1
        for j in range(13):
            prod = prod * sub[j]
        res.push_back(prod)
    cdef vector[long long].iterator it = max_element(res.begin(), res.end())
    return deref(it)


cdef long long greatestProduct(char * digits):
    cdef int i, n = strlen(digits)
    cdef int j
    cdef long long prod, maxProd = 0

    for i in range(n - 12):
        # printf("cur digits[i] %d\n", digits[i] - 48)
        # printf("cur digits[i+1] %d\n", digits[i + 1] - 48)
        # printf("cur digits[i+2] %d\n", digits[i + 2] - 48)
        # printf("cur digits[i+3] %d\n", digits[i + 3] - 48)
        # printf("cur digits[i+4] %d\n", digits[i + 4] - 48)
        # printf("cur digits[i+5] %d\n", digits[i + 5] - 48)
        # printf("cur digits[i+6] %d\n", digits[i + 6] - 48)
        # printf("cur digits[i+7] %d\n", digits[i + 7] - 48)
        # printf("cur digits[i+8] %d\n", digits[i + 8] - 48)
        # printf("cur digits[i+9] %d\n", digits[i + 9] - 48)
        # printf("cur digits[i+10] %d\n", digits[i + 10] - 48)
        # printf("cur digits[i+11] %d\n", digits[i + 11] - 48)
        # printf("cur digits[i+12] %d\n", digits[i + 12] - 48)
        prod = 1
        for j in range(13):
            prod *= (digits[i+j]-48)

        # printf("cur maxProd %d\n", maxProd)
        # printf("cur prod %d\n", prod)
        if prod > maxProd:
            maxProd = prod

    return maxProd


def max_multiply_v2():
    cdef str data
    cdef bytes data_b
    cdef char * c_string
    cdef long long res
    with open('ep08.txt', 'r') as f:
        data = ''
        for line in f.readlines():
            data = data + line.strip()
    data_b = bytes(data, encoding="utf-8")
    c_string = data_b
    res = greatestProduct(c_string)
    return res
