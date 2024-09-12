def solve():
    n, k = map(int, input().split())
    lst = [i for i in range(k, k + n)]
    
    # คำนวณค่าผลรวมทั้งหมด
    total_sum = sum(lst)
    
    # กำหนดค่าเริ่มต้นของ minV เป็นค่าผลรวมทั้งหมด
    minV = total_sum
    
    # ตรวจสอบการลบแต่ละค่าออกจากชุดและคำนวณผลรวม
    for i in range(n):
        new_sum = abs(total_sum - lst[i])
        if new_sum < minV:
            minV = new_sum
            
    print(minV)

# อ่านจำนวนเคส
for _ in range(int(input())):
    solve()
