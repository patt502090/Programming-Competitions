def solve():
    n, m = map(int, input().split())
    num = [int(x) for x in input().split()]
    ma = max(num)
    ans = []
    for _ in range(m):
        op, l, r = input().split()
        l, r = int(l), int(r)
        if l <= ma <= r:
            if op == "+":
                ma += 1
            else:
                ma -= 1
        ans.append(ma)
    
    print(' '.join(map(str,ans)))
 
for _ in range(int(input())):
    solve()
