from question1 import get_sum_multiples_py
from q1 import get_sum_multiples
import timeit


if __name__ == "__main__":
    sec0 = timeit.repeat('get_sum_multiples_py()', setup='from __main__ import get_sum_multiples_py', number=10000)
    print(f"get_sum_multiples cost {sec0} seconds")
    sec1 = timeit.repeat('get_sum_multiples()', setup='from __main__ import get_sum_multiples', number=10000)
    print(f"get_sum_multiples cost {sec1} seconds")

