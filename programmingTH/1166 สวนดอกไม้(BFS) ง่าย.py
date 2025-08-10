# โปรแกรมหาขนาดพื้นที่เชื่อมติดกันที่เหมาะจะทำ "สวนดอกไม้"
# ตามเงื่อนไข: ต้องเป็น '.' และห้ามติดกับ '#' (ห้ามอยู่ในช่องที่มีหินหรือช่องที่อยู่ติดกับหิน)
# รับข้อมูล: N M แล้วตามด้วย N บรรทัดของแผนที่ (แต่ละบรรทัดยาว M ตัวอักษร)
# คืนค่า: ขนาดที่มากที่สุดของพื้นที่ที่เป็นไปได้ (จำนวนช่อง)

from collections import deque

def largest_flower_garden(n, m, grid):
    """
    n, m : ขนาดตาราง (จำนวนแถว, จำนวนคอลัมน์)
    grid : รายการของสตริง length m แต่ละสตริงเป็น '.' หรือ '#'
    คืนค่า: ขนาดของกลุ่ม '.' ที่ใหญ่ที่สุดซึ่งไม่ติด '#' ใดๆ
    """
    # สร้างตารางบล็อก (True = ช่องนี้ไม่สามารถใช้ปลูกได้)
    # เราจะ mark ช่องที่เป็น '#' และช่องที่อยู่ติดกับ '#' เป็น blocked
    blocked = [[False] * m for _ in range(n)]

    # สี่ทิศ (บน ล่าง ซ้าย ขวา) สำหรับตรวจขอบเขตและสำรวจเพื่อนบ้าน
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # 1) ทำการ mark ช่องหิน '#' และช่องที่อยู่ติดกับหิน เป็น blocked
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':          # ถ้าช่องนี้เป็นหิน
                blocked[i][j] = True      # ช่องหินก็ไม่สามารถปลูกได้
                # mark ช่องรอบๆ (แต่ต้องเช็กขอบตาราง)
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m: # ไม่ใส่ไว้ index error เอาไว้กับออกขอบ
                        blocked[ni][nj] = True

    # 2) เราจะหา connected components ของช่อง '.' ที่ยังไม่ถูก blocked
    # ใช้ BFS เพื่อเดินสำรวจแต่ละกลุ่มและนับขนาด
    seen = [[False] * m for _ in range(n)]   # เก็บว่าช่องไหนเคยเข้า BFS แล้ว (visited)
    ans = 0  # เก็บขนาดสูงสุดที่เจอ

    for i in range(n):
        for j in range(m):
            # เงื่อนไขเริ่ม BFS: ต้องเป็นดิน '.' และไม่ blocked และยังไม่เคย seen
            if grid[i][j] == '.' and not blocked[i][j] and not seen[i][j]:
                q = deque()
                q.append((i, j))
                seen[i][j] = True
                component_size = 0

                # เริ่ม BFS นับขนาดกลุ่ม
                while q:
                    x, y = q.popleft()
                    component_size += 1

                    # ตรวจเพื่อนบ้าน 4 ทิศ
                    for di, dj in dirs:
                        nx, ny = x + di, y + dj
                        # เช็กขอบเขต, ยังไม่ seen, เป็น '.' และไม่ blocked
                        if (0 <= nx < n and 0 <= ny < m
                                and not seen[nx][ny]
                                and not blocked[nx][ny]
                                and grid[nx][ny] == '.'):
                            seen[nx][ny] = True
                            q.append((nx, ny))

                # อัปเดตคำตอบด้วยขนาดกลุ่มที่เจอ
                if component_size > ans:
                    ans = component_size

    return ans


if __name__ == "__main__":
    # อ่าน input
    n, m = map(int, input().split())
    grid = [input().rstrip() for _ in range(n)]
    # เรียกฟังก์ชันและพิมพ์คำตอบ
    print(largest_flower_garden(n, m, grid))
