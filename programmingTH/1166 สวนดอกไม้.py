from collections import deque

# Directions (down, right, up, left)
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

n, m = map(int, input().split())
arr = [[''] * (m + 2) for _ in range(n + 2)]
mark = [[0] * (m + 2) for _ in range(n + 2)]
ans = 0

# Read grid
for i in range(1, n + 1):
    row = input().strip()
    for j in range(1, m + 1):
        arr[i][j] = row[j - 1]

def bfs(i, j):
    global ans
    cnt = 0
    q = deque()
    q.append((i, j))
    mark[i][j] = 1

    while q:
        cnt += 1
        now_i, now_j = q.popleft()

        for k in range(4):
            ii = now_i + di[k]
            jj = now_j + dj[k]
            if ii < 1 or jj < 1 or ii > n or jj > m:
                continue
            if mark[ii][jj] or arr[ii][jj] != '.':
                continue
            mark[ii][jj] = 1
            q.append((ii, jj))

    ans = max(ans, cnt)

# Mark blocked and adjacent cells
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if arr[i][j] == '#':
            mark[i][j] = 1
            for k in range(4):
                ii = i + di[k]
                jj = j + dj[k]
                if ii < 1 or jj < 1 or ii > n or jj > m:
                    continue
                mark[ii][jj] = 1

# BFS for unvisited empty cells
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if arr[i][j] == '.' and mark[i][j] == 0:
            bfs(i, j)

print(ans)
