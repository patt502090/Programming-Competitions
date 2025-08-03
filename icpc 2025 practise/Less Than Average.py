import sys

data = []

try:
    for line in sys.stdin:
        parts = line.strip().split()
        data.extend(parts)
except EOFError:
    pass
xd =[ int(x ) for x in data]
ck = int(sum(xd) / len(xd))
cnt = 0
for x in xd:
    if x < ck:
        cnt += 1

print(cnt)