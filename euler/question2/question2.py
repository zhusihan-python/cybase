# 400 万之内所有偶数的斐波那契数字之和

def fib(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


def even_fibonacci_sum_py(n):
    total = 0
    for num in fib(n):
        if num % 2 == 0:
            total += num
    return total


if __name__ == "__main__":
    res = fib(20)
    print([r for r in res])
    print(even_fibonacci_sum_py(20))
