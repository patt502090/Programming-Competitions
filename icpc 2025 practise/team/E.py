import sys

data = []

try:
    for line in sys.stdin:
        data.extend(line.strip().split())
except EOFError:
    pass

n = int(data[0])

arr = list(map(int, data[1:n+1]))
print(arr)

mx = cur = arr[0]
for i in range(1, n):
    cur = max(arr[i], cur + arr[i])
    mx = max(mx, cur)
print(mx)
