def solve():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        k = int(data[index + 1])
        index += 2
        
        if n % 2 == 0:
            results.append(1)
        else:
            results.append((n % 2) % 2)
    
    print("\n".join(map(str, results)))

