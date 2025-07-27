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
input = lambda: sys.stdin.readline().rstrip("\r\n")
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input())
LII = lambda: list(map(int, input().split()))
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LGMI = lambda: list(map(lambda x: int(x) - 1, input().split()))

MOD1, MOD9 = 10**9 + 7, 998244353
Y, N = "Yes", "No"



def solve():
    n = II()
    a = LII()
    d = deque(a)
    q = []
    ans = []

    def is_bad(arr):
        if len(arr) < 5:
            return False
        inc = all(arr[i] < arr[i + 1] for i in range(4))
        dec = all(arr[i] > arr[i + 1] for i in range(4))
        return inc or dec

    while d:
        if not q:
            q.append(d.popleft())
            ans.append('L')
            continue

        if len(d) == 1:
            q.append(d.popleft())
            ans.append('L')
            continue
            
        can_l, can_r = True, True
        if len(q) >= 4:
            if is_bad(q[-4:] + [d[0]]):
                can_l = False
            if is_bad(q[-4:] + [d[-1]]):
                can_r = False

        if can_l and can_r:
            if abs(d[0] - q[-1]) < abs(d[-1] - q[-1]):
                q.append(d.popleft())
                ans.append('L')
            else:
                q.append(d.pop())
                ans.append('R')
        elif can_l:
            q.append(d.popleft())
            ans.append('L')
        elif can_r:
            q.append(d.pop())
            ans.append('R')
        else:
            q.append(d.popleft())
            ans.append('L')

    print("".join(ans))

if __name__ == "__main__":
    try:
        TEST = II()
        for _ in range(TEST):
            solve()
    except (IOError, ValueError):
        pass