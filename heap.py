import heapq
n = int(input())
min_heap = []
sol = []
for i in range(n):
  process = input().split()
  if process[1]:
    heapq.heappush(min_heap, -int(process[1]))
  else:
    if not min_heap:
      print("-1")
    else :
      c = -heapq.heappop(min_heap)
      print(c)

