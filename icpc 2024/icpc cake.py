def calculate_max_deliciousness(N):
    # ถ้าจำนวนชิ้นเค้กน้อยกว่า 3 จะไม่สามารถกินได้ตามกฎ
    if N < 3:
        return 0

    total_deliciousness = 0

    # คำนวณค่าความอร่อยจากการกินชิ้นเค้กที่ดีที่สุด
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if j != i:
                total_deliciousness += abs(i - j)

    return total_deliciousness


# Test example
N = 10
print(calculate_max_deliciousness(N))  # ควรจะได้ 74
