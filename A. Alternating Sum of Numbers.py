def solve():
   n = int(input())
   lst = [int(x) for x in input().split()]
   sum = 0
   if n == 1:
       return lst[0]
   for i in range(1,n):
     if i == 1:
        sum = lst[i-1] - lst[i]
     elif i % 2 == 0:
         sum += lst[i]
     else :
         sum -= lst[i]

   return sum
for _ in range(int(input())):
   print(solve())
