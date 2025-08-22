import math

def ones_in_r(n, m, k):
    d = abs(n - m)             
    combs = [math.comb(k, i) for i in range(k + 1)]
    max_bitlen = max(c.bit_length() for c in combs) 

    if d >= max_bitlen:
        return sum(c.bit_count() for c in combs)

    S = 0
    for i, c in enumerate(combs):
        S += c << (d * i)
    return S.bit_count()

n, m, k = map(int, input().split())
print(ones_in_r(n, m, k))
