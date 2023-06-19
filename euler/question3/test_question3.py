from question3 import max_prime_factor_py
from q3 import max_prime_factor
import timeit


if __name__ == "__main__":
    sec0 = timeit.repeat('max_prime_factor_py(600851475143)', setup='from __main__ import max_prime_factor_py', number=1000)
    print(f"max_prime_factor_py cost {sec0} seconds")
    sec2 = timeit.repeat('max_prime_factor(600851475143)', setup='from __main__ import max_prime_factor', number=1000)
    print(f"max_prime_factor cost {sec2} seconds")
