n,t = [int(x) for x in input().split()]
lst = []
for i in range(t):
    lst.append(input().split(maxsplit=1))
lst.sort(reverse = True,key = lambda x: int(x[0]))
sum = 0
for i in range(n):
    sum += int(lst[i][0])
print(sum)
ans = []
for i in range(n):
    ans.append(str(lst[i][1]))
for i in ans[::-1]:
    print(i)
    



#============version สั้นๆ by chatgpt================
# n, t = map(int, input().split())
# lst = [input().split(maxsplit=1) for _ in range(t)]

# # เรียงลำดับตามตัวเลขและคำนวณผลรวม
# lst.sort(reverse=True, key=lambda x: int(x[0]))

# # คำนวณผลรวมและพิมพ์คำตอบ
# print(sum(int(x[0]) for x in lst[:n]))
# print("\n".join(x[1] for x in lst[:n][::-1]))
