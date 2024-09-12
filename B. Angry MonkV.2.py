def solve():
    n, k = map(int,input().split())
    num = [int(x) for x in input().split()]
    count = 0
    num.sort()
    for i in range(k-1):
        count += 2 * num[i] - 1 
    print(count)
for _ in range(int(input())):
    solve()
