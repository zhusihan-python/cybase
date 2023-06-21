# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
import math
from sympy import primerange
from math import log, ceil


def is_prime(number):
    if number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(number) + 1), 2):
            if number % i == 0:
                return False
    return True


def prime_number_py():
    n = 3
    i = 2
    while i < 10002:
        if is_prime(n):
            i += 1
        n += 2
    return n - 2


# 经测试 比纯py版本慢50%
def prime_number_pure_math(n=10001):
    upper_bound = ceil((log(n)+log(log(n))) * n)
    primes = list(primerange(1, upper_bound))
    return primes[n-1]


def prime_number_py_v2():
    primes = [2]
    attempt = 3
    while len(primes) < 10001:
        if all(attempt % prime != 0 for prime in primes):
            primes.append(attempt)
        attempt += 2
    return primes[-1]


# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes/
def primes_sieve_py(n):
    p_n = int(2 * n * math.log(n))       # over-estimate p_n
    sieve = [True] * p_n                 # everything is prime to start
    count = 0
    for i in range(2, p_n):
        if sieve[i]:                       # still prime?
            count += 1                     # count it!
            if count == n:                 # done!
                return i
            for j in range(2*i, p_n, i):   # cross off all multiples of i
                sieve[j] = False


if __name__ == "__main__":
    print(prime_number_py())
    print(prime_number_pure_math())
    print(primes_sieve_py(10001))
