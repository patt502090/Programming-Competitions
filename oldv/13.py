def check(e):
    for i in range(2,e):
        if e % i == 0:
            return False
        else :
            return True
n = int(input())
count = 0
all = set()
while True:
    w = [int(x) for x in input().split()]
    for l in w:
        if l == 2:
            all.add(2)
        if l == 1:
            all.add(1)
        if check(l) == True:
            all.add(l)
    count += len(w)
    if count == n:
        break
c = list(all)
c.sort()
print(len(c))
for i in c:
    print(i)
