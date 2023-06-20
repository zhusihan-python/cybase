# 求两个 3 位数之积最大的回文数


def is_palindromic(n):
    n_str = str(n)
    return n_str == n_str[::-1]


# 经测试 比字符串操作慢一倍多
def is_palindromic_v2(n):
    original_n = n
    reversed_n = 0
    while n > 0:
        rem = n % 10
        reversed_n = reversed_n * 10 + rem
        n = n // 10
    return original_n == reversed_n


def max_palindromic_py():
    max_palindromic = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            prod = i * j
            if is_palindromic(prod) and prod > max_palindromic:
                max_palindromic = prod
    return max_palindromic


def max_palindromic_rev():
    max_palindromic = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            prod = i * j
            if is_palindromic(prod) and prod > max_palindromic:
                max_palindromic = prod
                break
    return max_palindromic


if __name__ == "__main__":
    print(max_palindromic_rev())
