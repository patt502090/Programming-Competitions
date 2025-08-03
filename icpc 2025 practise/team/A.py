n = int(input())
lst = []
for _ in range(n):
    line = input().split()
    g, s, b = map(int, line[:3])
    name = " ".join(line[3:])
    lst.append([g, s, b, name])

lst.sort(key=lambda x: (-x[0], -x[1], -x[2], x[3]))

for i, team in enumerate(lst, 1):
    g, s, b, name = team
    total = g + s + b
    print(f"{i}: {name} {g} {s} {b} {total}")
