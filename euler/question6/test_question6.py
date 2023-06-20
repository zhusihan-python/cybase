from question6 import difference_py
from q6 import difference
import timeit


if __name__ == "__main__":
    # print(difference_py())
    # print(difference())
    sec = timeit.repeat('difference_py()', setup='from __main__ import difference_py', number=1000)
    print(f"difference_py cost {sec} seconds")
    sec = timeit.repeat('difference()', setup='from __main__ import difference', number=1000)
    print(f"difference cost {sec} seconds")
