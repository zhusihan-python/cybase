from question2 import even_fibonacci_sum_py
from q2 import even_fibonacci_sum, even_fibonacci_sum_v2
import timeit


if __name__ == "__main__":
    sec0 = timeit.repeat('even_fibonacci_sum_py(4000000)', setup='from __main__ import even_fibonacci_sum_py', number=10000)
    print(f"even_fibonacci_sum_py cost {sec0} seconds")
    sec2 = timeit.repeat('even_fibonacci_sum(4000000)', setup='from __main__ import even_fibonacci_sum', number=10000)
    print(f"even_fibonacci_sum cost {sec2} seconds")
    sec3 = timeit.repeat('even_fibonacci_sum_v2(4000000)', setup='from __main__ import even_fibonacci_sum_v2', number=10000)
    print(f"even_fibonacci_sum_v2 cost {sec3} seconds")
