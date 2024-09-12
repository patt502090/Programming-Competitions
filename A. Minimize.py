def solve():
    n = int(input())
    results = []

    for i in range(n):
        ans = []
        word = str(input())
        lst = [str(x) for x in word]
        for k in range(4):  
            if lst[k] == "#":
                ans.append(4-k)
                break
        
        results.append(" ".join(map(str, ans)))

    print(" ".join(results))

for _ in range(int(input())):
    solve()
