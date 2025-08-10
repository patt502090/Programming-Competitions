 ImportType = InputType = ConstType = 1
  DecoratorType = FunctinoType = 1

   # print(list(map(sum,zip(*cnt))))
   # print("YES" if sum(map(sum,zip(*cnt))) == 0 else "NO")

   # print("YES" if sum(cnt) == 0 else "NO")

   # A. Arrival of the General (NinePon)
   # def solve():
   #     n = II()
   #     lst = LII()
   #     cnt = 0
   #     mx = max(lst)
   #     mn = min(lst)
   #     i = 0

   #     for i in range(n):
   #         if lst[i] == mx:
   #             while i > 0:
   #                 lst[i],lst[i-1] = lst[i-1],lst[i]
   #                 cnt += 1
   #                 i -= 1
   #             break
   #     for i in range(n-1,-1,-1):
   #         if lst[i] == mn:
   #             while i <= n - 1:
   #                 lst[i],lst[i+1] = lst[i+1],lst[i]
   #                 i += 1
   #                 cnt += 1
   #             break

   #     print(cnt)

   # " WUBIWEBAM to "I AM" "
   # print(' '.join(word.replace("WUB"," ").split()))

   if ImportType:
        import os
        import sys
        import random
        import threading
        from copy import deepcopy
        from decimal import Decimal, getcontext
        from random import randint, choice, shuffle
        from types import GeneratorType
        from functools import lru_cache, reduce
        from bisect import bisect_left, bisect_right
        from collections import Counter, defaultdict, deque
        from itertools import accumulate, combinations, permutations
        from heapq import heapify, heappop, heappush, heappushpop
        from typing import Generic, Iterable, Iterator, TypeVar, Union, List
        from string import ascii_lowercase, ascii_uppercase, digits
        from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
        from sys import stdin, stdout, setrecursionlimit

    if InputType:
        def input(): return sys.stdin.readline().rstrip("\r\n")
        def I(): return input()
        def II(): return int(input())
        def MII(): return map(int, input().split())
        def LI(): return list(input())
        def LII(): return list(map(int, input().split()))
        def GMI(): return map(lambda x: int(x) - 1, input().split())
        def LGMI(): return list(map(lambda x: int(x) - 1, input().split()))

    if FunctinoType:

        class Math:
            __slots__ = ["mod", "l", "fact", "inv"]

            def __init__(self):
                self.mod = mod = 10**9 + 7
                self.l = l = 3 * 10**5 + 5
                self.fact = fact = [1] * (l + 1)
                self.inv = inv = [1] * (l + 1)
                for i in range(1, l + 1):
                    fact[i] = fact[i - 1] * i % mod
                inv[l] = pow(fact[l], mod - 2, mod)
                for i in range(l - 1, -1, -1):
                    inv[i] = inv[i + 1] * (i + 1) % mod

            def comb(self, n: int, r: int):  # (Combination) CNR เลขจัดหมู่
                return (self.fact[n] * self.inv[r] %
                         self.mod * self.inv[n - r] %
                    self.mod if n >= r >= 0 else 0 )

            def perm(self, n: int, r: int):  # (Permutation) PNR เลขเรียงสับเปลี่ยน
                return self.fact[n] * self.inv[n -
                                               r] % self.mod if n >= r >= 0 else 0

            # math_obj = Math()
            # combination = math_obj.comb(5, 2)  # คำนวณค่า C(5, 2) = 10
            # permutation = math_obj.perm(5, 2)  # คำนวณค่า P(5, 2) = 20

    if ConstType:
        MOD1, MOD9 = 10**9 + 7, 998244353
        RD = random.randint(MOD1, MOD1 << 1)
        Direction4 = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # ->, <-, v, ^
        Direction8 = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]  # ->, <-, v, ^, ↘, ↙, ↗, ↖
        Y, N = "Yes", "No"
        A, B = "Alice", "Bob"

    def remove_duplicates(lst):
        seen = set()
        result = []

        for item in lst:
            if item not in seen:
                result.append(item)
                seen.add(item)

        return result

    #  n = II()
    #     v = sorted(LII())
    #     l, r, x = 0, 2000000, -1

    #     while l <= r:
    #         rich = l + (r - l) // 2
    #         b = v[:]
    #         b[-1] += rich
    #         total_sum = sum(b)
    #         avg_wealth = total_sum / n
    #         counter = 0
    #         for wealth in b:
    #             if wealth < avg_wealth / 2.0:
    #                 counter += 1
    #         if counter > n // 2:
    #             x = rich
    #             r = rich - 1
    #         else:
    #             l = rich + 1

    #     print(x)

    # n = II()
    # lst = sorted(LII(),reverse = True)
    # cnt = 0
    # ck = 0
    # for i in range(len(lst)):
    #     if lst[i] > 2 and ck == 0 and lst[i] <= 4:
    #         cnt += 1
    #     else:
    #         ck == lst[i]
    #         if lst[i] + ck > 3 and ck:
    #             cnt += 1
    #             ck = 0
    #         else:
    #             ck += lst[i]

    # print(cnt)

    def solve():
        x = [int(x) for x in input().split()]
        print(
            min(
                abs(x[0] - x[2]) + abs(x[1] - x[2]),
                abs(x[0] - x[1]) + abs(x[1] - x[2]),
                abs(x[0] - x[1]) + abs(x[0] - x[2]),
            )
        )
        # print((abs(x[0] - x[2]) + abs(x[1] - x[2]), abs(x[0] - x[1]) + abs(x[1] - x[2])))

# solution
# *l,=map(int,input().split());print(max(l)-min(l))

    if __name__ == "__main__":
        # TESTS = II()
        for _ in range(1):
            solve()

        # print(cnt)

        # print(lst.count(max(lst)))
