n = int(input())
Adrian = ['A', 'B', 'C']*n
Bruno = ['B', 'A', 'B', 'C']*n
Goran = ['C', 'C', 'A', 'A', 'B', 'B']*n
scores = {'Adrian':0, 'Bruno':0, 'Goran':0}
key = input()
for i in range(n):
    if (Adrian[i] == key[i]):
        scores['Adrian'] += 1
    if (Bruno[i] == key[i]):
        scores['Bruno'] += 1
    if (Goran[i] == key[i]):
        scores['Goran'] += 1
tmp = max(scores.values())
print(tmp)
for name, score in scores.items():
    if score == tmp:
        print(name)