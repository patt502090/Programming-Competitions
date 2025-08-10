import sys

data = []

try:
    for line in sys.stdin:
        parts = line.strip().split()
        data.extend(parts)
except EOFError:
    pass

n = int(data[0])

data = list(map(int, data[1:n + 1]))

cnt = 0
cl = int(sum(data) / len(data))
for i in data:
    if i >= cl:
        cnt += 1
print(cnt)
