n, m = map(int, input().split())
k = int(input())

# สร้างกระดานเริ่มต้น
board = [[0 for _ in range(m)] for _ in range(n)]

# วางระเบิด
for _ in range(k):
    x, y = map(int, input().split())
    board[x][y] = '*'
    # เพิ่มรอบๆ ระเบิด
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != '*':
                board[nx][ny] += 1

# แสดงผลลัพธ์
for row in board:
    print(''.join(str(cell) for cell in row))
