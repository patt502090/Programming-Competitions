import heapq
import sys

input = sys.stdin.read  # ใช้ sys.stdin.read เพื่ออ่านข้อมูลทั้งหมดในครั้งเดียว

def main():
    data = input().split()  # อ่านข้อมูลทั้งหมดในครั้งเดียวและแยกเป็นลิสต์
    n = int(data[0])  # จำนวนคำสั่ง
    min_heap = []
    index = 1

    for _ in range(n):
        if data[index] == 'P':
            value = int(data[index + 1])
            heapq.heappush(min_heap, -value)
            index += 2
        elif data[index] == 'Q':
            if not min_heap:
                print("-1")
            else:
                print(-heapq.heappop(min_heap))
            index += 1

if __name__ == "__main__":
    main()
