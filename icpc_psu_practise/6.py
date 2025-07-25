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