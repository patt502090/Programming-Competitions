import sys
input = sys.stdin.readline

N = int(input())
A = []

for i in range(N):
    x = int(input())
    A.append(x)

A.sort()

if N <= 2:
    print(N)
    sys.exit()

ans = 2
R = 1

for L in range(N - 1):
    R = max(R, L + 1)
    while R + 1 < N and A[L] + A[L + 1] > A[R + 1]:
        R += 1
    ans = max(ans, R - L + 1)

print(ans)
