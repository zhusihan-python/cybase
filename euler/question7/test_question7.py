from question7 import prime_number_py, prime_number_pure_math
import timeit


if __name__ == "__main__":
    sec0 = timeit.repeat('prime_number_py()', setup='from __main__ import prime_number_py', number=10)
    print(f"prime_number_py cost {sec0} seconds")
    sec0 = timeit.repeat('prime_number_pure_math()', setup='from __main__ import prime_number_pure_math', number=10)
    print(f"prime_number_pure_math cost {sec0} seconds")
