from collections import defaultdict


def main():
    t = 1  # จำนวนเทสเคส (โจทย์นี้มีแค่ 1 เทสเลย fix ไว้)
    # t = inpu()  # ต้นฉบับจะใช้ input หลายเคส (แต่คอมเมนต์ไว้เฉยๆ)

    for _ in range(t):  # วนทำ t รอบ
        n = input()  # จำนวนพนักงานทั้งหมด
        g = defaultdict(list)  # สร้างกราฟแบบ dictionary ที่เก็บ list (ใช้แทน adjacency list)

        # รับข้อมูลหัวหน้าของพนักงานแต่ละคน
        for i in range(n):
            s = input()  # s คือหัวหน้าของพนักงาน i+1 (index เริ่มจาก 0)
            if s != -1:
                g[i + 1].append(s)  # เพิ่มขอบในกราฟ: พนักงาน i+1 ถูกเชื่อมกับหัวหน้า s

        q = []  # queue สำหรับเก็บ node ที่อยู่ระดับล่างสุดใน tree

        # ค้นหาพนักงานที่มี "ลูกน้องแค่คนเดียว"
        for i in g:
            if len(g[i]) == 1:
                q.append(i)  # เพิ่มใน queue เริ่มต้น

        visited = [False] * (n + 1)  # สร้าง visited สำหรับกันวนซ้ำ
        h = 0  # ตัวแปรนับ "จำนวนชั้นความลึก" → คือจำนวนกลุ่มที่ต้องใช้

        # เริ่ม BFS ทีละชั้น
        while q:
            h += 1  # เพิ่มชั้นความลึก
            s = []  # queue ชั่วคราวสำหรับชั้นถัดไป

            while q:
                ss = q.pop(0)  # ดึง node ปัจจุบันจาก queue
                # visited[ss] = True  # (ถูกคอมเมนต์ไว้) ถ้าเปิดจะกันซ้ำ

                # วนลูกน้องของ node นี้ (เช่น หัวหน้า → ลูกน้อง)
                for i in g[ss]:
                    if not visited[i]:  # ถ้ายังไม่เคยไป
                        s.append(i)  # เตรียมไว้สำหรับรอบหน้า
                        # visited[i] = True  # (ถูกคอมเมนต์ไว้)

            q = s  # เตรียม queue สำหรับรอบถัดไป (ลึกลงอีกชั้น)

        # ถ้า h = 0 แปลว่าไม่มีใครมีหัวหน้า → ทุกคน root เองหมด → ต้องมี 1 กลุ่ม
        if h == 0:
            print(1)
        else:
            print(h)

# เรียก main() ตอนรัน script
if __name__ == '__main__':
    main()
