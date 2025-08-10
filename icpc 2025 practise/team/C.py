import math


def cal(x, tri=0):
    if x <= 2:
        return tri
    y = (-1 + math.sqrt(1 + (8 * x))) / 2
    y = math.floor(y)
    tri += (y - 1) ** 2
    jud = (y * (y + 1)) / 2
    return cal(x - jud, tri)


t = int(input())
for i in range(t):
    print(cal(int(input()), 0))
