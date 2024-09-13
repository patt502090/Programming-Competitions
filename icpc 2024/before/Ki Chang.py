import math
N, M, H, Q = map(int, input().split())
distance = [list(map(int, input().split())) for _ in range(N)]
net = list(map(int, input().split()))
quest = [list(map(int, input().split())) for _ in range(Q)]

for _ in quest:
  count_x = 0
  c = distance.copy()
  n = net.copy()
  ch = True
  if _[0] == len(distance):
    c.sort(reverse=True, key=lambda x: x[0] + x[1])
    n.sort(reverse = True)
  else :
    c.sort(key= lambda x: x[1])
    n.sort()
  for i in range(_[0]):
    if c[i][1] - H > n[i]:
      print("-1")
      ch = False
      break
    else:
      count = 0
      for net_value in n:
        if c[i][1] - H <= net_value:
          count += 1
          n.remove(net_value)
          break
      if count > 0:
        count_x = c[i][0]
  if ch:
    print(count_x)



