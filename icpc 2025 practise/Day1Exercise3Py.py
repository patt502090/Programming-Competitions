n, M = map(int, input().split())
lst = sorted(map(int, input().split()))

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
