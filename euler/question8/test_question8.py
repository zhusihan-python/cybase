from question8 import max_multiply_py
from q8 import max_multiply, max_multiply_v2
import timeit


if __name__ == "__main__":
    sec = timeit.repeat('max_multiply_py()', setup='from __main__ import max_multiply_py', number=100)
    print(f"max_multiply_py cost {sec} seconds")
    sec = timeit.repeat('max_multiply()', setup='from __main__ import max_multiply', number=100)
    print(f"max_multiply cost {sec} seconds")
    sec = timeit.repeat('max_multiply_v2()', setup='from __main__ import max_multiply_v2', number=100)
    print(f"max_multiply_v2 cost {sec} seconds")
    # max_multiply_v2 25 times faster than max_multiply_py
