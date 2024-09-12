def solve():
    results = []
    n = int(input()) 
    ans = []
    for i in range(n):
        ck = input().strip()  
        findA = ck.index('#') + 1
        ans.append(findA)
        
    print(" ".join(map(str, ans[::-1])))
    
for _ in range(int(input())):
    solve()
