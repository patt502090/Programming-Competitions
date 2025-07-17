def solve():
  n = int(input())
  lst = [int(x) for x in input().split()]
  loop = int(input())
  for i in range(loop):
    word = str(input())
    if len(word) != n:
        print("No")
    else :
        last = set(zip(lst,[str(x) for x in word]))
        count = []
        for i in last:
            count.append(sum(1 for _, char in last if char == i[1]))
            
        for i in count:
            if i > 1:
                print("No")
                break
            elif i == 1:
                continue
        else:
            print("YES")
    

for _ in range(int(input())):
  solve()
