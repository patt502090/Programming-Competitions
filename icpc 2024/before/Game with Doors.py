n = int(input())
for k in range(n):
    Alice = []
    Bob = []
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    i = 0
    k = 0
    T = True
    Y = True
    while T:
        if len(Alice) == 0:
            Alice.append((A[0]+i, A[0]+i+1))
            i += 1
        elif len(Alice) > 0 and Alice[-1][1] - A[1] < 1:
            Alice.append((A[0]+i, A[0]+i+1))
            i += 1
        else:
            if A[0] > B[0]:
                c = A[0]-B[0]
                for x in range(1,c):
                    Alice.append((A[0]-x, A[0]-x+1))
            T = False
            
    while Y:
        if len(Bob) == 0:
            Bob.append((B[0]+k-1, B[0]+k))
            k += 1
            
        elif len(Bob) > 0 and Bob[-1][1] - B[1] < 0:
            Bob.append((B[0]+k-1, B[0]+k))
            k += 1
        else:
            Y = False
    Pair = [item for item in Alice if item in Bob]
    print(len(Pair))
