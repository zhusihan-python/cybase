from question4 import max_palindromic_py, max_palindromic_rev
from q4 import max_palindromic, max_palindromic_v2, max_palindromic_v3
import timeit


if __name__ == "__main__":
    print(max_palindromic())
    print(max_palindromic_v2())
    print(max_palindromic_v3())
    # sec = timeit.repeat('max_palindromic_py()', setup='from __main__ import max_palindromic_py', number=1)
    # print(f"max_palindromic_py cost {sec} seconds")
    # sec = timeit.repeat('max_palindromic_rev()', setup='from __main__ import max_palindromic_rev', number=1)
    # print(f"max_palindromic_rev cost {sec} seconds")
    # sec = timeit.repeat('max_palindromic()', setup='from __main__ import max_palindromic', number=1)
    # print(f"max_palindromic cost {sec} seconds")
    # sec = timeit.repeat('max_palindromic_v2()', setup='from __main__ import max_palindromic_v2', number=1)
    # print(f"max_palindromic_v2 cost {sec} seconds")
    # sec = timeit.repeat('max_palindromic_v3()', setup='from __main__ import max_palindromic_v3', number=1)
    # print(f"max_palindromic_v3 cost {sec} seconds")
