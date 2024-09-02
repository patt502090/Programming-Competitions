def solve():
    n,s,m = [int(x) for x in input().split()]
    task = [list(map(int,input().split())) for _ in range(n)]
    task.sort(key = lambda x: x[0])
    ck = True
    
    if task[0][0] >= s:
        print("Yes")
        return
    
    for i in range(1,n):
        if task[i][0] - task[i-1][1] >= s:
            print("Yes")
            return
            
    if  m - task[-1][1] >=  s :
        print("Yes")
        return
        
    if ck:
        print("No")
                
for _ in range(int(input())):
    solve()
