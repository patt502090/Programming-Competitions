def mxd(n, cases):
    result = []
    for case in cases:
        count = case[0]
        prices = case[1:]
        
        if count < 4:
            result.append(0)
            continue
        prices.sort(reverse=True)
        total_discount = 0
        for i in range(0, count, 4):
            if i + 3 < count:
                total_discount += prices[i + 3]
        
        result.append(total_discount)
    
    return result


n = int(input())

cases = []
for _ in range(n):
    case = list(map(int, input().split()))
    cases.append(case)

results = mxd(n, cases)

for result in results:
    print(result)
