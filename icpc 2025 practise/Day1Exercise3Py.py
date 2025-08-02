n, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()  

total_time = 0     
score = 0           
count = 0           

for t in lst:
    if total_time + t > M:
        break
    total_time += t
    score += total_time
    count += 1

print(count, score)
