MOD = 1_000_000_009

n = int(input().strip())
ans = (pow(2, n + 1, MOD) - ((n + 2) % MOD)) % MOD
print(ans)
