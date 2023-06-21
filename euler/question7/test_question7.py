from question7 import prime_number_py, prime_number_pure_math, prime_number_py_v2, primes_sieve_py
from q7 import primes_sieve_list, primes_sieve_vector
import timeit


if __name__ == "__main__":
    # print(prime_number_py())
    # print(prime_number())
    sec = timeit.repeat('prime_number_py()', setup='from __main__ import prime_number_py', number=1)
    print(f"prime_number_py cost {sec} seconds")
    sec = timeit.repeat('prime_number_pure_math()', setup='from __main__ import prime_number_pure_math', number=1)
    print(f"prime_number_pure_math cost {sec} seconds")
    sec = timeit.repeat('prime_number_py_v2()', setup='from __main__ import prime_number_py_v2', number=1)
    print(f"prime_number_py_v2 cost {sec} seconds")
    sec = timeit.repeat('primes_sieve_py(10001)', setup='from __main__ import primes_sieve_py', number=1)
    print(f"primes_sieve_py cost {sec} seconds")
    sec = timeit.repeat('primes_sieve_list(10001)', setup='from __main__ import primes_sieve_list', number=1)
    print(f"primes_sieve_list cost {sec} seconds")
    sec = timeit.repeat('primes_sieve_vector(10001)', setup='from __main__ import primes_sieve_vector', number=1)
    print(f"primes_sieve_vector cost {sec} seconds")
