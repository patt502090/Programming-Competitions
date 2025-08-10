import sys
import math

data = []

try:
    for line in sys.stdin:
        parts = line.strip().split()
        data.append(list(map(int, parts)))
except EOFError:
    pass
data.pop(-1)
mx = float('-inf')
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        x1, y1, z1 = data[i]
        x2, y2, z2 = data[j]

        d = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5

        mx = max(mx, d)

print(f"{mx:.2f}")
