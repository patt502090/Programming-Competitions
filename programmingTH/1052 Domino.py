n = int(input())
dominoes = []

for _ in range(n):
    x, h = map(int, input().split())
    dominoes.append((x, h))

def fall_right(dominoes, start):
    count = 1
    reach = dominoes[start][0] + dominoes[start][1]
    i = start + 1
    while i < n and dominoes[i][0] < reach:
        count += 1
        reach = max(reach, dominoes[i][0] + dominoes[i][1])
        i += 1
    return count

def fall_left(dominoes, start):
    count = 1
    reach = dominoes[start][0] - dominoes[start][1]
    i = start - 1
    while i >= 0 and dominoes[i][0] > reach:
        count += 1
        reach = min(reach, dominoes[i][0] - dominoes[i][1])
        i -= 1
    return count

max_fallen = 0
best_index = 0
best_dir = 'L'

for i in range(n):
    current_r = fall_right(dominoes, i)
    current_l = fall_left(dominoes, i)
    
    if current_r > current_l:
        current_max = current_r
        current_dir = 'R'
    elif current_l > current_r:
        current_max = current_l
        current_dir = 'L'
    else:
        current_max = current_r
        current_dir = 'L'
    
    # Update the best overall choice
    if current_max > max_fallen:
        max_fallen = current_max
        best_index = i
        best_dir = current_dir
    elif current_max == max_fallen:
        if i < best_index:
            best_index = i
            best_dir = current_dir
        elif i == best_index:
            if current_dir == 'L':
                best_dir = 'L'

print(f"{best_index + 1} {best_dir}")