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
    q = deque(a)

    ans = []
    cnt = 0
    is_max = True
    for _ in range(n):
        if is_max:
            if q[0] > q[-1]:
                ans.append("L")
                q.popleft()
            else:
                ans.append("R")
                q.pop()

        else:
            if q[0] > q[-1]:
                ans.append("R")
                q.pop()
            else:
                ans.append("L")
                q.popleft()

        is_max = not is_max

    print("".join(ans))


if __name__ == "__main__":
    try:
        TEST = II()
        for _ in range(TEST):
            solve()
    except (IOError, ValueError):
        pass
