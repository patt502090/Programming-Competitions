import sys
from collections import defaultdict, deque
data = []

try:
    for line in sys.stdin:
        data.extend(line.strip().split())
except EOFError:
    pass

n = int(data[0])
arr = list(map(str, data[1:n + 1]))
need = list(map(str, data[n + 1::]))
graph = defaultdict(list)
print(need)
for i in need:
    graph[need] =
