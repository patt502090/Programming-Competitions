from collections import deque
n = int(input())
for _ in range(n):
    lst = [int(x) for x in input().split()]
    lst = deque(lst)
    ck = lst[0]
    mn = 0
    cnt = 0
    while lst:
        ckx = lst.pop()
        if ckx > mn:
            cnt += 1 
            mn = ckx
    print(f"Case {_+1}: {cnt}")