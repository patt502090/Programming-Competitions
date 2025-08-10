n = int(input())
all = []
for i in range(n):
    lst = [str(x) for x in input().split()]
    all.append(lst)

all = sorted(all, key=lambda x: (x[3], x[2], x[1], x[0]), reverse=True)
# all = sorted(all,key = lambda x:x[3])
# for i in range(2,-1,-1):
# all = sorted(all,key = lambda x:x[i], reverse = True)


print(all)
