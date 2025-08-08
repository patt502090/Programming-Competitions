n = int(input())
dominoes = [tuple(map(int, input().split())) for _ in range(n)]

def fall_right(i):
    count = 1
    reach = dominoes[i][0] + dominoes[i][1]
    j = i + 1
    while j < n and dominoes[j][0] < reach:
        count += 1
        reach = max(reach, dominoes[j][0] + dominoes[j][1])
        j += 1
    return count

def fall_left(i):
    count = 1
    reach = dominoes[i][0] - dominoes[i][1]
    j = i - 1
    while j >= 0 and dominoes[j][0] > reach:
        count += 1
        reach = min(reach, dominoes[j][0] - dominoes[j][1])
        j -= 1
    return count

best = (0, 'L', 1)  # (จำนวนที่ล้มได้, ทิศ, index)

for i in range(n):
    r = fall_right(i)
    l = fall_left(i)

    if r > best[0] or (r == best[0] and i < best[2]):
        best = (r, 'R', i)
    if l > best[0] or (l == best[0] and i < best[2]):
        best = (l, 'L', i)

print(best[2] + 1, best[1])
