from question8 import max_multiply_py
from q8 import max_multiply
import timeit


if __name__ == "__main__":
    # print(max_multiply_py())
    # print(max_multiply())
    sec = timeit.repeat('max_multiply_py()', setup='from __main__ import max_multiply_py', number=100)
    print(f"max_multiply_py cost {sec} seconds")
    sec = timeit.repeat('max_multiply()', setup='from __main__ import max_multiply', number=100)
    print(f"max_multiply cost {sec} seconds")
