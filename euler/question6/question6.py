# 求 1 到 100 自然数的“和的平方”与“平方和”的差

def difference_py():
    pow_of_sum = pow(sum([i for i in range(1, 101)]), 2)
    sum_of_pow = sum([i**2 for i in range(1, 101)])
    return pow_of_sum - sum_of_pow


if __name__ == "__main__":
    print(difference_py())
