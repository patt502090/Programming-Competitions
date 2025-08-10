n, m = [int(x) for x in input().split()]
ans = 0
for i in range(n, m + 1):
    ans += i
print(ans)
