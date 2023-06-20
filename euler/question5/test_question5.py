from question5 import min_multiply_py, min_multiply_v2
from q5 import min_multiply, min_multiply_v3
import timeit


if __name__ == "__main__":
    # print(min_multiply_v2())
    # print(min_multiply())
    sec = timeit.repeat('min_multiply_py()', setup='from __main__ import min_multiply_py', number=10)
    print(f"min_multiply cost {sec} seconds")
    sec = timeit.repeat('min_multiply_v2()', setup='from __main__ import min_multiply_v2', number=10)
    print(f"min_multiply_v2 cost {sec} seconds")
    sec = timeit.repeat('min_multiply()', setup='from __main__ import min_multiply', number=10)
    print(f"min_multiply cost {sec} seconds")
    sec = timeit.repeat('min_multiply_v3()', setup='from __main__ import min_multiply_v3', number=10)
    print(f"min_multiply_v3 cost {sec} seconds")
