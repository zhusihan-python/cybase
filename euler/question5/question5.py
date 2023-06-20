# 找出能够被 1, 2, 3, ..., 20 整除的最小整数

def can_divide_1_to_20(number):
    for i in range(1, 21):
        if number % i != 0:
            return False
    return True


def min_multiply_py():
    start = 1710
    step = 1710
    while not can_divide_1_to_20(start):
        start += step

    return start


# https://stackoverflow.com/questions/10093613/optimising-code-to-find-the-lowest-number-divisible-by-all-integers-between-1-20
def min_multiply_v2():
    prime_array = [2, 3, 5, 7, 11, 13, 17, 19]
    result = 1
    for prime in prime_array:
        p = prime
        while p * prime < 20:
            p *= prime
        result *= p
    return result


if __name__ == "__main__":
    print(min_multiply_py())
