def solve():
    n, k = map(int, input().split())
    lst = []
    
    for i in range(k,k+n):
        lst.append(i)
        
    minV = sum(lst)
    #print(minV)
    for i in range(len(lst)):
        count = 0
        
        for j in range(len(lst)):
            if i <= j :
                count = count - lst[j]
            else:
                count = count + lst[j]
            #print(f'{i},{j} : {count}')
  
        if abs(count) < minV:
            minV = abs(count)
            
    print(minV)   
        
for _ in range(int(input())):
    solve()
