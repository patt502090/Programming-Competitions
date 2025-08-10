import sys
sys.setrecursionlimit(10000)  # กัน recursion เกินลิมิต (แต่โจทย์นี้ไม่เกินอยู่แล้วเพราะ 30x30 = 900 ช่อง)

def largest_flower_garden_dfs(n, m, grid):
    """
    n, m  : ขนาดตาราง (จำนวนแถว, จำนวนคอลัมน์)
    grid  : list ของ string แต่ละตัวอักษรเป็น '.' หรือ '#'
    return: ขนาดของพื้นที่ที่ใหญ่ที่สุด (จำนวนช่อง) ที่ใช้ปลูกได้
    """

    # blocked[i][j] = True หมายถึง ช่องนี้ "ใช้ไม่ได้" (เป็นหินหรืออยู่ติดกับหิน)
    blocked = [[False] * m for _ in range(n)]

    # ทิศทาง 4 ทิศ (บน, ล่าง, ซ้าย, ขวา)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # 1) Mark ช่อง '#' และช่องที่อยู่ติดกับ '#' เป็น blocked
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                blocked[i][j] = True
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m:
                        blocked[ni][nj] = True

    # ตาราง seen สำหรับเก็บว่าช่องนี้เคยเข้า DFS แล้วหรือยัง
    seen = [[False] * m for _ in range(n)]

    def dfs(x, y):
        """
        ฟังก์ชัน DFS: เดินหาช่องที่อยู่ในกลุ่มเดียวกัน
        x, y : ตำแหน่งปัจจุบัน
        return: จำนวนช่องในกลุ่มที่พบจากจุดนี้
        """
        seen[x][y] = True   # mark ว่าเจอแล้ว
        size = 1            # เริ่มนับช่องนี้ 1 ช่อง

        # เดินสำรวจเพื่อนบ้าน 4 ทิศ
        for di, dj in directions:
            nx, ny = x + di, y + dj
            if (0 <= nx < n and 0 <= ny < m
                    and not seen[nx][ny]
                    and not blocked[nx][ny]
                    and grid[nx][ny] == '.'):
                size += dfs(nx, ny)  # บวกจำนวนช่องจากการเดินต่อ
        return size

    # หาขนาดกลุ่มที่ใหญ่ที่สุด
    max_size = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.' and not blocked[i][j] and not seen[i][j]:
                group_size = dfs(i, j)  # นับขนาดกลุ่มด้วย DFS
                if group_size > max_size:
                    max_size = group_size

    return max_size


if __name__ == "__main__":
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    print(largest_flower_garden_dfs(n, m, grid))
