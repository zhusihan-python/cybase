from libcpp.vector cimport vector
from libcpp.algorithm cimport max_element
from cython.operator cimport dereference as deref

def max_multiply():
    cdef int i
    cdef int len_data
    cdef long long prod
    cdef list sub
    with open('ep08.txt', 'r') as f:
        data = ''
        for line in f.readlines():
            data = data + line.strip()
    len_data = len(data)
    cdef vector[long long] res

    for i in range(988):
        sub = [ <long long>int(data[i+j]) for j in range(13) ]
        prod = 1
        for j in range(13):
            prod = prod * sub[j]
        res.push_back(prod)
    cdef vector[long long].iterator it = max_element(res.begin(), res.end())
    return deref(it)