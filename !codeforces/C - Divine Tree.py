def comp(a, b):
    # จัดลำดับ: first มากกว่า มาก่อน / ถ้าเท่ากัน ดู second น้อยกว่า มาก่อน
    if a[0] > b[0]:
        return -1
    elif a[0] == b[0]:
        if a[1] < b[1]:
            return -1
        else:
            return 1
    else:
        return 1


def solve():
    n, m = map(int, input().split())
    vec = []

    # เงื่อนไขว่าไม่มีทางสร้างต้นไม้ที่มี divineness รวมเป็น m ได้
    if m < n or m > n * (n + 1) // 2:
        print(-1)
        return

    m -= n  # หักค่า default ของ d(v)=1 ออกก่อน

    for i in range(n):
        index = i + 1  # Node หมายเลข 1-based
        c = min(i, m)
        vec.append([c, index])
        m -= c

    # sort โดยใช้ key ที่เลียนแบบ comp จาก C++
    vec.sort(key=lambda x: (-x[0], x[1]))

    print(vec[0][1])  # พิมพ์ root

    for i in range(n - 1):
        print(vec[i][1], vec[i + 1][1])


# main
t = int(input())
for _ in range(t):
    solve()
