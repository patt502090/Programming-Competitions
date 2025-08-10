for _ in range(int(input())):
    k = int(input())
    n = [str(x) for x in input()]
    print("No" if n[0] == n[-1] else "Yes")
