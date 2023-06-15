# 求小于 1000 的能被 3 或 5 整除的所有整数之和

def get_sum_multiples_py():
    sum = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum
