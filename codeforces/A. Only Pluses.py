def solve():
    A = [int(x) for x in input().split()]
    for i in range(5):
        x = min(A)
        c = A.index(x)
        A[c] += 1
    print(A[0] * A[1] * A[2])
for _ in range(int(input())):
    solve()
