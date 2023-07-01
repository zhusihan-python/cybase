# 在 1000 位的大整数里找到相邻的 13 个数字
from functools import reduce


def max_multiply_py():
    with open('ep08.txt', 'r') as f:
        data = ''
        for line in f.readlines():
            data = data + line.strip()
    res = []
    for i in range(988):
        sub = [int(x) for x in data[i:i+13]]
        prod = reduce(lambda x, y: x*y, sub)
        res.append(prod)
    return max(res)


if __name__ == "__main__":
    print(max_multiply_py())
