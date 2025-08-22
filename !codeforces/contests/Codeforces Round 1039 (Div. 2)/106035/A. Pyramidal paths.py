def is_pyramidal(a):
    n = len(a)
    inc = a[1] > a[0]
    i = 1
    
    while i < n and ((a[i] > a[i-1]) if inc else (a[i] < a[i-1])):
        i += 1
        
    if i == n:
        return False
    
    while i < n and ((a[i] < a[i-1]) if inc else (a[i] > a[i-1])):
        i += 1
        
    return i == n

n = int(input().strip())
lst = list(map(int, input().split()))
print("YES" if is_pyramidal(lst) else "NO")
