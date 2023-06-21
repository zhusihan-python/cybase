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


if __name__ == "__main__":
    print(prime_number_py())
    print(prime_number_pure_math())
