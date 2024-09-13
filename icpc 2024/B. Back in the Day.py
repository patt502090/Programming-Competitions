ImportType = InputType = ConstType = 1
DecoratorType = FunctinoType = 1
if ImportType:
   import os, sys, random, threading
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
   input = lambda: sys.stdin.readline().rstrip("\r\n")
   I = lambda: input()
   II = lambda: int(input())
   MII = lambda: map(int, input().split())
   LI = lambda: list(input())
   LII = lambda: list(map(int, input().split()))
   GMI = lambda: map(lambda x: int(x) - 1, input().split())
   LGMI = lambda: list(map(lambda x: int(x) - 1, input().split()))

if FunctinoType:
    class Math:
        __slots__ = ["mod", "l", "fact", "inv"]
        
        def __init__(self):
            self.mod = mod = 10 ** 9 + 7
            self.l = l = 3 * 10 ** 5 + 5
            self.fact = fact = [1] * (l + 1)
            self.inv = inv = [1] * (l + 1)
            for i in range(1, l + 1):
                fact[i] = fact[i - 1] * i % mod
            inv[l] = pow(fact[l], mod - 2, mod)
            for i in range(l - 1, -1, -1):
                inv[i] = inv[i + 1] * (i + 1) % mod
        
        def comb(self, n: int, r: int): #(Combination) CNR เลขจัดหมู่
            return self.fact[n] * self.inv[r] % self.mod * self.inv[n - r] % self.mod if n >= r >= 0 else 0
        
        def perm(self, n: int, r: int): #(Permutation) PNR เลขเรียงสับเปลี่ยน
            return self.fact[n] * self.inv[n - r] % self.mod if n >= r >= 0 else 0
        
        #math_obj = Math()
        #combination = math_obj.comb(5, 2)  # คำนวณค่า C(5, 2) = 10
        #permutation = math_obj.perm(5, 2)  # คำนวณค่า P(5, 2) = 20
        
if ConstType:
    MOD1, MOD9 = 10 ** 9 + 7, 998244353
    RD = random.randint(MOD1, MOD1 << 1)
    Direction4 = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # ->, <-, v, ^
    Direction8 = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]  # ->, <-, v, ^, ↘, ↙, ↗, ↖
    Y, N = "Yes", "No"
    A, B = "Alice", "Bob"

def check(lst):
    ans = []
    perf = len(lst) // (3 if lst[0] not in ["7","9"] else 4)
    remain = 0
    if lst[0] not in ['7','9']:
        remain = len(lst) % 3
        if lst[0] == "1":
            pass
        if lst[0] == "2":
            if remain == 1: ans.append("a")
            if remain == 2: ans.append("b")
        if lst[0] == "3":
            if remain == 1: ans.append("d")
            if remain == 2: ans.append("e")
        if lst[0] == "4":
            if remain == 1: ans.append("g")
            if remain == 2: ans.append("h")
        if lst[0] == "5":
            if remain == 1: ans.append("j")
            if remain == 2: ans.append("k")
        if lst[0] == "6":
            if remain == 1: ans.append("m")
            if remain == 2: ans.append("n")
        if lst[0] == "8":
            if remain == 1: ans.append("t")
            if remain == 2: ans.append("u")
    else:
        remain = len(lst) % 4
        if lst[0] == "7":
            if remain == 1: ans.append("p")
            if remain == 2: ans.append("q")
            if remain == 3: ans.append("r")
        if lst[0] == "9":
            if remain == 1: ans.append("w")
            if remain == 2: ans.append("x")
            if remain == 3: ans.append("y")

    for i in range(perf):
        if lst[0] not in ['7','9']:
            if lst[0] == "1":
                pass
            if lst[0] == "2":
                ans.append("c")
            if lst[0] == "3":
                ans.append("f")
            if lst[0] == "4":
                ans.append("i")
            if lst[0] == "5":
                ans.append("l")
            if lst[0] == "6":
                ans.append("o")
            if lst[0] == "8":
                ans.append("v")
        else:
            if lst[0] == "7":
                ans.append("s")
            if lst[0] == "9":
                ans.append("z")
    return ''.join(ans)


def solve():
    num =I()
    ck = []
    for i in range(len(num)):
        if i == len(num)-1:
            ck.append(num[i])
            break
        elif num[i] == num[i+1]:
            ck.append(num[i])
        elif num[i] != num[i+1]:
            ck.append(num[i])
            print(check(ck),end = '')
            ck = []

    if ck:
       print(check(ck),end = '')

 
if __name__ == '__main__':
   TEST = 1
   for _ in range(TEST):
      solve()