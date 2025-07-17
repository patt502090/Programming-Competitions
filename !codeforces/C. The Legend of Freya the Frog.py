import math
def solve():
    n, m, k = map(int,input().split())
    ckX = math.ceil(n/k)
    ckY = math.ceil(m/k)
    if ckX > ckY:
        print((ckX * 2)-1)
    else:
        print(ckY * 2)

for _ in range(int(input())):
    solve()
