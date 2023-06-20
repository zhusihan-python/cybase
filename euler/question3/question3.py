# 找出整数 600851475143 的最大素数因子
import math


def is_prime(number):
    if number == 2:
        return True
    elif number % 2 == 0:
        return True
    else:
        for i in range(3, int(math.sqrt(number) + 1), 2):
            if number % i == 0:
                return False
    return True


def max_prime(number):
    result = 0
    for i in range(2, number):
        if number % i == 0 and is_prime(i):
            if i > result:
                result = i

    return result


# 1. 从2到sqrt(n)的范围内,一定包含n的至少一个质因子(如果n是完全数则包含全部质因子)。
# 2. 找到一个质因子后,算法会不断将n除以该质因子,直到n不能被该质因子整除。
# 3. 如果除尽后n变为1,则该质因子就是最大质因子。如果n仍大于1,则n本身就是最大质因子。
# 4. 因此,无论最大质因子是不是大于sqrt(n),这个算法都能找到它。
# 举个例子,对于n = 10:
# 1. 从2到sqrt(10) = 3之间,2是10的质因子
# 2. 将10不断除以2,得到5
# 3. 5不能被2整除,此时n > 1,所以最大质因子是n本身,也就是5
# 可以看出,虽然5比sqrt(10)还大,但由于找到2后将10不断化简,最终只剩5,所以仍然得出了正确结果。
# 同样的,对于n = 15:
# 1. 从2到3之间,找到质因子3
# 2. 将15除以3得到5
# 3. 5不能被3整除,且n > 1,所以最大质因子是5
# 可以总结为:从2到sqrt(n)之间一定能找到一个质因子,找到后化简n直至只剩最大质因子,无论该质因子是否大于sqrt(n),算法都能正确求出最大质因子。
def max_prime_factor_py(n):
    if n <= 1:
        return 0
    num = None
    for i in range(2, n):
        if i * i > n:
            break
        while n % i == 0:
            num = i
            n = n // i
    if n > 1:
        num = n
    return num


if __name__ == "__main__":
    print(max_prime_factor_py(600851475143))
