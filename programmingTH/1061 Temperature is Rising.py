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
    from string import (
        ascii_lowercase,
        ascii_uppercase,
        digits,
        punctuation,
        printable,
        whitespace,
    )


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
            return (
                self.fact[n] * self.inv[r] % self.mod * self.inv[n - r] % self.mod
                if n >= r >= 0
                else 0
            )

        def perm(self, n: int, r: int):  # (Permutation) PNR เลขเรียงสับเปลี่ยน
            return self.fact[n] * self.inv[n - r] % self.mod if n >= r >= 0 else 0

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

def solve():
    
        
    
if __name__ == "__main__":
    TEST = II()
    for _ in range(TEST):
        solve()
  

