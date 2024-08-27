n = int(input())
all = []
for i in range(n):
  lst = [str(x) for x in input().split()]
  all.extend(lst)
i = 0
while i < len(all)-1:
  if all[i] == all[i+1]:
    all.pop(i)
    all.pop(i)
    if i != 0:
      i -= 1
  else :
    i += 1

print(len(all))
print("".join(all[::-1]) if len(all) != 0 else 'empty')
  
