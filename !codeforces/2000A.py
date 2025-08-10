import sys


def EOF():
    for _ in sys.stdin:
        yield _


n = int(next(EOF()))
for i in range(n):
    x, y = [int(x) for x in next(EOF()).split()]
    if x < y:
        print(x, y)
    else:
        print(y, x)
