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
graph = defaultdict(list)
# print(n)
# print(arr)
need = list(map(str, data[n + 1::]))
# print(need)
for word in arr:
    for i in range(len(word)):
        tf = word[:i] + "*" + word[i + 1:]
        graph[tf].append(word)

for ex in need:
    if ex == need[0]:
        continue
    visited = set()
    queue = deque([(need[0], 1)])
    while queue:
        wd, dt = queue.popleft()

        if word == ex:
            print(dt)
            exit()

        visited.add(wd)

        for i in range(len(wd)):
            tf = wd[:i] + "*" + word[i + 1:]

            powx = graph.get(tf, None)

            if powx:
                for wo in powx:
                    if wo not in visited:
                        queue.append((wo, dt + 1))
                        visited.add(wo)
