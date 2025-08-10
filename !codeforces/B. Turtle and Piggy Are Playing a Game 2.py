def solve():
    n = int(input())
    seq = [int(x) for x in input().split()]

    while len(seq) > 1:
        for i in range(n - 1):
            if i % 2 != 0:
                seq.remove(max(seq[0], seq[1]))
            else:
                seq.remove(min(seq[0], seq[1]))

    print(seq[0])


for _ in range(int(input())):
    solve()
