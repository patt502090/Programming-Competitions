from collections import defaultdict, OrderedDict, Counter, deque
from itertools import permutations, combinations, product
import math
from pprint import pprint 
# from queue import PriorityQueue
import threading
import sys
from bisect import bisect_left, bisect_right, insort_left
from heapq import heappush, heappop
import heapq
# from sympy import primepi

MOD = 998244353
# MOD = 10**9 + 7
# MOD = 998244353

sys.setrecursionlimit(10**5)
threading.stack_size(10**6)
input = sys.stdin.readline
flush = sys.stdout.flush

def lower_bound(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] >= target:
            r = mid - 1
        else:
            l = mid + 1
    return l
    
def upper_bound(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return r
  
def find_prime_factors(n):
    factors = defaultdict(int)
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            factors[divisor] += 1
            n //= divisor
        divisor += 1

    if n > 1:
        factors[n] += 1

    return factors
 
def find_divisors(n):
    sqrt = math.isqrt(n)
    divs = []
    for div in range(1, sqrt+1):
        if n % div == 0:
            divs.append(div)
            if div != n // div:
                divs.append(n // div)
    
    # divs.sort()        
    return divs
    
def is_prime(n):
    if n == 1 or n == 0: return False
    sq = math.isqrt(n)
    for div in range(2, sq+1):
        if n % div == 0:
            return False
    return True
 
def soe(start, limit):
    # Initialize a boolean array to mark prime numbers
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    
    # Perform Sieve of Eratosthenes
    for i in range(2, math.isqrt(limit) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    # Collect primes within the specified range
    primes = []
    for i in range(start, limit + 1):
        if is_prime[i]:
            primes.append(i)
    
    return primes

  
def ceil_division(a, b):
    return (a+b-1)//b
 
def get_triangle_area(x, y):
    area = 0.5 * (x[0] * (y[1] - y[2]) + x[1] * (y[2] - y[0]) + x[2] * (y[0] - y[1]))
    return area
    
def prefix_sum(arr):
    prx = []
    cur = 0
    for num in arr:
        cur += num
        # cur %= m
        prx.append(cur)
    return prx
  
def prefix_max(arr):
    prx = []
    mx = float("-inf")
    for num in arr:
        mx = max(mx, num)
        prx.append(mx)
    return prx

def prefix_min(arr):
    prx = []
    mn = float("inf")
    for num in arr:
        mn = min(mn, num)
        prx.append(mn)
    return prx
  
def prefixSum2D(a, R, C):
    psa = [[0 for x in range(C)] for y in range(R)]
    psa[0][0] = a[0][0]
  
    for i in range(1, C):
        psa[0][i] = (psa[0][i - 1] + a[0][i])
    for i in range(1, R):
        psa[i][0] = (psa[i - 1][0] + a[i][0])
  
    for i in range(1, R):
        for j in range(1, C):
            psa[i][j] = (psa[i - 1][j] + psa[i][j - 1] - psa[i - 1][j - 1] + a[i][j])
    return psa

def sum_interval_2d(prx, row1, col1, row2, col2):
    to_remove_first = prx[row1 - 1][col2] if row1 > 0 else 0
    to_remove_second = prx[row2][col1 - 1] if col1 > 0 else 0
    common = prx[row1 - 1][col1 - 1] if (row1 > 0 and col1 > 0) else 0
    return prx[row2][col2] - to_remove_first - to_remove_second + common

    
def sum_interval(prx, start, end):
    if start > end: return 0
    end = min(len(prx) - 1, end)
    start = max(0, start)
    return prx[end] - prx[start-1] if start > 0 else prx[end]
 
def quadratic_formula(a, b, c):
    ans1 = (-b + (b**2 - 4*a*c)**0.5) // (2*a)
    ans2 = (-b - (b**2 - 4*a*c)**0.5) // (2*a)
    return ans1, ans2
 
def is_between(i1, j1, i2, j2, i3, j3):
    collinear = (j2 - j1) * (i3 - i1) == (j3 - j1) * (i2 - i1)
    
    if not collinear:
        return False
    
    within_bounds = (min(i1, i3) <= i2 <= max(i1, i3)) and (min(j1, j3) <= j2 <= max(j1, j3))
    
    return within_bounds
 
def slope(x1, y1, x2, y2):
    if x2 == x1: return float("inf")
    x = (y2 - y1) / (x2 - x1)
    return x
 
def get_counts(arr):
    counts = defaultdict(int)
    for num in arr:
        counts[num] += 1
    return counts
  
def gcd_arr(arr):
    gcd = arr[0]
    for num in arr:
        gcd = math.gcd(gcd, num)
    return gcd
 
# CONST = (1 << 31) - 1
 
def lcm(*integers):
    a = integers[0]
    for b in integers[1:]:
        a = (a * b) // math.gcd (a, b)
    return a
 
def get_inverse(n):
    global CONST
    return n ^ CONST
  
def is_palindrome(arr):
    return arr == arr[::-1]
  
# def is_kalindrome(arr, x, l, r):
#     while l <= r:
#         if arr[l] == arr[r]:
#             l += 1
#             r -= 1
#         else:
#             if arr[l] == x:
#                 l += 1
#             elif arr[r] == x:
#                 r -= 1
#             else:
#                 return False
#     return True
 
def suffix_sum(arr):
    sm = 0
    ans = []
    rev_arr = arr[::-1]
    for num in rev_arr:
        sm += num
        ans.append(sm)
    return ans[::-1]

def suffix_max(arr):
    mx = float("-inf")
    ans = []
    rev_arr = arr[::-1]
    for num in rev_arr:
        mx = max(mx, num)
        ans.append(mx)

    return ans[::-1]
  
def suffix_min(arr):
    mn = float("inf")
    ans = []
    rev_arr = arr[::-1]
    for num in rev_arr:
        mn = min(mn, num)
        ans.append(mn)

    return ans[::-1]

def kadanes_algo(arr):
    sm = 0
    mx = float("-inf")
    ans = []
    for num in arr:
        sm += num
        if sm < 0:
            sm = 0
        mx = max(mx, sm)
        ans.append(mx)
    return ans

def kadanes_algo_neg(arr):
    sm = 0
    mn = float("inf")
    ans = []
    for num in arr:
        sm += num
        if sm > 0:
            sm = 0
        mn = min(mn, sm)
        ans.append(mn)
    return ans

def arithmitic_seq_sum(a, b, n):
    return (n * (a + b)) // 2
  
def geometric_seq_sum(a, b, r):
    return (b*r - a) // (r - 1)


def find_diff_char(forbidden_chars):
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in forbidden_chars:
            return char
    return ""
  
def mod_inverse_euclidean(a, mod):
    g, x, y = extended_gcd(a, mod)
    if g != 1:
        raise ValueError(f"No modular inverse for {a} under mod {mod}")
    else:
        return x % mod

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return g, x, y
    
def sum_law(n):
    if n <= 0: return 0
    return (n * (n + 1)) // 2

def sum_law_diff(l, r):
    return sum_law(r) - sum_law(l-1)

def factorial(start, n, m):
    while n > 1:
        start *= n
        start %= m
        n -= 1

    return start

def lcm_arr(arr):
    ans = 1
    for num in arr:
        ans = lcm(ans, num)

    return ans

def findProductSum(A, n): 
      
    # calculating array sum (a1 + a2 ... + an) 
    array_sum = 0
    for i in range(0, n, 1): 
        array_sum = array_sum + A[i] 
  
    # calculating square of array sum 
    # (a1 + a2 + ... + an)^2 
    array_sum_square = array_sum * array_sum 
  
    # calculating a1^2 + a2^2 + ... + an^2 
    individual_square_sum = 0
    for i in range(0, n, 1): 
        individual_square_sum += A[i] * A[i] 
  
    # required sum is (array_sum_square - 
    # individual_square_sum) / 2 
    return (array_sum_square - 
            individual_square_sum) // 2


# found = defaultdict(list)

# N = 1001  # Replace with the desired value of N
# d = [N] * N
# d[1] = 0

# for i in range(1, N):
#     for x in range(1, i + 1):
#         j = i + i // x
#         if j < N:
#             d[j] = min(d[j], d[i] + 1)


    



# print(costs[:20])

# print(costs[:30])

ceil_division
# def knapsack(k, weights, gains):
#     n = len(weights)
#     # Create a DP table with k+1 capacity (0 to k)
#     dp = [[0] * (k + 1) for _ in range(n + 1)]
    
#     # Iterate through items
#     for i in range(1, n + 1):
#         for w in range(k + 1):
#             if weights[i-1] <= w:  # If the current item can be included
#                 dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + gains[i-1])
#             else:
#                 dp[i][w] = dp[i-1][w]  # Cannot include the item, carry forward the previous value
    
#     # The answer will be in dp[n][k], i.e., considering all items and capacity k
#     return dp[n][k]


def knapsack_optimized(k, weights, gains):
    n = len(weights)
    dp = [0] * (k + 1)
    
    for i in range(n):
        for w in range(k, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + gains[i])
    
    return dp[k]


def knapsack_optimized_min(k, weights, gains):
    n = len(weights)
    dp = [float("inf")] * (k + 1)
    
    for i in range(n):
        for w in range(k, weights[i] - 1, -1):
            dp[w] = min(dp[w], dp[w - weights[i]] + gains[i])
    
    # print(dp)
    return dp[k]


# def power(n, p, m=MOD):
#     if p == 0:
#         return 1
#     if p < 0:
#         return 0
    
#     if (p & 1 == 0):
#         term = power(n, (p >> 1), m) % m
#         return (term * term) % m
#     else:
#         return ((n % m) * power(n, p - 1, m)) % m
    

def power(x, y, mod=MOD):
    res = 1
    while y:
        if y & 1:
            res = res * x % mod
        x = x * x % mod
        y //= 2
    return res


def get_diagonals(matrix):
    rows, cols = len(matrix), len(matrix[0])
    diagonals = []

    # Under and mid
    for j in range(rows):
        diagonal = [matrix[i][i - j] for i in range(j, rows)]
        diagonals.append(diagonal)
    
    # Above
    for j in range(1, cols):
        diagonal = [matrix[i][i + j] for i in range(rows - j)]
        diagonals.append(diagonal)

    return diagonals

def get_mode(arr):
    arr.sort()
    mode = arr[0]
    h_freq = 1
    cur_freq = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            cur_freq += 1
            if cur_freq > h_freq:
                h_freq = cur_freq
                mode = arr[i]
        else:
            cur_freq = 1

    return mode

def loop_spiral(matrix, n, m):

    rows, cols = n, m
    top, bottom, left, right = 0, rows - 1, 0, cols - 1
    spiral_order = []
    # print(n, m)
    idxes = []

    layers = []
    num_layers = min(n, m) // 2
    for _ in range(num_layers):
        layer = []
        # print(spiral_order)
        # TOP ROW
        for i in range(left, right + 1):
            # print(top, i, matrix)
            layer.append(matrix[top][i])
            idxes.append([top, i])

        top += 1

        # print(spiral_order)
        
        # RIGHT COLUMN
        for i in range(top, bottom + 1):
            layer.append(matrix[i][right])
            idxes.append([i, right])

        right -= 1

        # print(spiral_order)

        # BOTTOM ROW
        for i in range(right, left - 1, -1):
            layer.append(matrix[bottom][i])
            idxes.append([bottom, i])


        bottom -= 1

        # print(spiral_order)
           
        # LEFT COLUMN
        for i in range(bottom, top - 1, -1):
            layer.append(matrix[i][left])
            idxes.append([i, left])

        
        left += 1
        layers.append(layer.copy())

        

    return layers, idxes

def xor_upto(n):
    if n % 4 == 0:
        return n
    elif n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n + 1
    else:
        return 0

def xor_range(l, r):
    return xor_upto(r) ^ xor_upto(l - 1)

def read_numbers(infile=None):
    return list(map(int, input().strip().split())) if infile == None else list(map(int, infile.readline().strip().split()))

def read_int(infile=None):
    return int(eval(input().strip())) if infile == None else int(eval(infile.readline().strip()))

def read_str(infile=None):
    return input().strip() if infile == None else infile.readline().strip()

def get_median(numbers):
    if not numbers:
        return None  # Handle the empty list case

    numbers = sorted(numbers)  # Sort the list
    n = len(numbers)

    # If the list length is odd, return the middle element
    if n % 2 == 1:
        return numbers[n // 2]
    # If the list length is even, return the average of the two middle elements
    else:
        mid1 = numbers[n // 2 - 1]
        mid2 = numbers[n // 2]
        return mid1
    
def factorial_mod(n, m):
    """Calculates n! % m iteratively."""
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % m
    return result

def mod_inverse_euclidean(a, m):
    """Calculates modular inverse of a under modulo m using Extended Euclidean algorithm."""
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError("Modular inverse does not exist")
    return x % m

def extended_gcd(a, b):
    """Helper function to find gcd and coefficients of Bezout's identity."""
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def comb_optimized(n, r, m):
    if n == r or r == 0:
        return 1
    if r > n:
        return 0
    # Calculate n!, r!, and (n-r)! % m
    n_fact = factorial_mod(n, m)
    r_fact = factorial_mod(r, m)
    nr_fact = factorial_mod(n - r, m)

    # Calculate modular inverse of r! and (n-r)! modulo m
    r_fact_inv = mod_inverse_euclidean(r_fact, m)
    nr_fact_inv = mod_inverse_euclidean(nr_fact, m)

    # Calculate the result
    return (n_fact * r_fact_inv % m) * nr_fact_inv % m

def build_full_ones(limit):
    full_ones = []
    cur = 1
    for _ in range(limit):
        full_ones.append(cur)
        cur |= (cur << 1)

    return full_ones


# three_powers = []
# cur = 1
# limit = 10**24
# while cur <= limit:
#     three_powers.append(cur)
#     cur *= 3


# ans = []
# i = 0
# limit = 1000000
# # print("da")
# while True:
#     b = bin(i)
#     s = str(b)[2:]
#     cur = 0
#     # print("la")
#     for j in range(len(s) - 1, -1, -1):
#         if s[j] == "1":
#             cur += (three_powers[len(s) - 1 - j])

#     # print(cur)
#     if cur > limit: break
#     ans.append(cur)
#     # print(cur)
#     i += 1
# m = 10**18
# print(ans)

# print(divs)




def log2_ceil(x):
    if x <= 1:
        return 0 
    
    
    bits = x.bit_length() - 1
    
    if x == (1 << bits):
        return bits
    return bits + 1




# powers = [1]
# cur = 1
# last = 1
# limit = 10**12
# while True:
#     cur += last
#     powers.append(cur)
#     if cur >= limit: break
#     last *= 2

# print(powers[:10])

# MOD = 10**9 + 7
# limit = 10**6 + 1
# dp = [0] * limit
# for num in range(1, limit):
#     if 1 <= num <= 6:
#         dp[num] += 1

#     for dec in range(1, 6 + 1):
#         if num - dec >= 0:
#             dp[num] += dp[num - dec]

#     dp[num] %= MOD

# print(dp[:10])

# factorials = [1]
# cur = 1
# for num in range(1, 200000 + 7):
#     cur *= num
#     factorials.append(cur)
#     cur %= MOD


def common(xl1, xl2, xr1, xr2, yl1, yl2, yr1, yr2):
    xlc = max(xl1, xl2)
    xrc = min(xr1, xr2)
    ylc = max(yl1, yl2)
    yrc = min(yr1, yr2)

    return xlc, ylc, xrc, yrc

def mex(arr):
    n = len(arr)
    present = [False] * (n + 1) 

    for num in arr:
        if 0 <= num <= n:  
            present[num] = True

    for i in range(n + 1):
        if not present[i]:
            return i

    return n + 1

def prefix_xor(arr):
    xor_res = 0
    res = []
    for num in arr:
        xor_res ^= num
        res.append(xor_res)

    return res

def xor_interval(prx, start, end):
    if start > end: return 0
    end = min(len(prx) - 1, end)
    start = max(0, start)
    return prx[end] ^ prx[start-1] if start > 0 else prx[end]


def add(a, b, m):
    h = a + b
    if h >= m:
        h -= m

    if h < 0:
        h += m

    return h

# int mul(int a, int b) {
#     return (a * 1LL * b) % MOD;
# }

def mul(a, b, m):
    return ((a % m) * (b % m)) % m

def count_children(adj, n, parents):
    num_children = [0] * (n + 1)
    for u in range(1, n + 1):
        for v in adj[u]:
            if v != parents[u]:  # Only count actual children, not back edges
                num_children[u] += 1
    return num_children


# def multinomial_coefficient(n, *groups):
#     """
#     Computes the multinomial coefficient:
#     C(n; k1, k2, ..., km) = n! / (k1! * k2! * ... * km!)
    
#     using an optimized iterative approach to avoid large factorial computations.
#     """
#     result = 1
#     k_sum = 0  # Tracks the cumulative sum of k1, k2, ...

#     for k in groups:
#         for i in range(k):
#             result *= (n - k_sum)  # Multiply numerator step by step
#             result //= (i + 1)  # Divide denominator step by step
#             k_sum += 1  # Keep track of how many elements are processed

#     return result

def compute_factorial_ratio(n, *groups):
    """ Computes (n!) / (k1! * k2! * ... * km!) efficiently. """
    result = 1
    k_sum = 0  # Tracks cumulative sum of k1, k2, ..., km

    for k in groups:
        for i in range(k):
            if n - k_sum > 0:  # Ensure numerator doesn't go negative
                result *= (n - k_sum)
            result //= (i + 1)  # Integer division to keep precision
            k_sum += 1  # Update processed elements

    return result

def count_inversions(arr):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left, inv_left = merge_sort(arr[:mid])
        right, inv_right = merge_sort(arr[mid:])
        merged, inv_split = merge(left, right)

        return merged, inv_left + inv_right + inv_split

    def merge(left, right):
        merged = []
        i = j = inv_count = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inv_count += len(left) - i  # All remaining elements in left are greater
                j += 1

        merged += left[i:]
        merged += right[j:]
        return merged, inv_count

    _, total_inversions = merge_sort(arr)
    return total_inversions


def max_2p(num):
    return num.bit_length() - 1



class SparseTable:

    '''
    This is a custom SparseTable that I made :)  mostafa_alaa99
    '''

    def __init__(self, a, n, f):
        self._f = f
        self._table = self._make_sparse_table(a, n, f)

    def _make_sparse_table(self, a, n, f):

        mx_2p = max_2p(n)
        matrix = [[0 for _ in range(n)] for _ in range(mx_2p + 1)]
        for j in range(n):
            matrix[0][j] = a[j]

        for j in range(1, mx_2p + 1):
            for i in range(n - (1 << j) + 1):
                left = matrix[j - 1][i]
                right = matrix[j - 1][i + (1 << (j - 1))]
                matrix[j][i] = f(left, right)

        return matrix
  
    def query(self, l, r):
        length = r - l + 1
        mx_2p = max_2p(length)
        left = self._table[mx_2p][l]
        right = self._table[mx_2p][r - (1 << mx_2p) + 1]
        return self._f(left, right)
    

class FenwickTreeNonIdempotent:

    
    '''
    This is a custom FenwickTree that I made :)  mostafa_alaa99
    '''

    def __init__(self, a, n, f, inv_f):
        self._n = n
        self._a = a
        self._f = f
        self._inv_f = inv_f
        self._fenwick_tree = self._construct_fenwick_tree(a, n, f, inv_f)

    def largest_2power_factor(k):
        return k & (-k)

    def _construct_fenwick_tree(self, a, n, f, inv_f):


        tree = [0] * n
        prx = []
        cur = 0
        for i in range(n):
            cur = f(cur, a[i])
            prx.append(cur)

        for i in range(n):
            length = FenwickTreeNonIdempotent.largest_2power_factor(i + 1)
            tree[i] = prx[i]
            start_interval = i - length + 1
            if start_interval > 0:
                tree[i] = inv_f(tree[i], prx[start_interval - 1])

        return tree
    
    def update(self, k, u):

        # All of them refer to the intervals that will be affected by this update
        
        prev = self._a[k]
        # First thing remove prev from all of them
        i = k
        while i < self._n:
            self._fenwick_tree[i] = self._inv_f(self._fenwick_tree[i], prev)
            i += FenwickTreeNonIdempotent.largest_2power_factor(i + 1)



        # Second thing add u to all of them
        i = k
        while i < self._n:
            self._fenwick_tree[i] = self._f(self._fenwick_tree[i], u)
            i += FenwickTreeNonIdempotent.largest_2power_factor(i + 1)

        self._a[k] = u

    def _query_helper(self, n):
        """
        Calculate the answer from 1 to n both inclusive
        """
        length = n + 1
        ans = 0
        i = 0
        while length > 0:
            max_p2 = int(math.log2(length))
            i += ((1 << max_p2) - 1)
            ans = self._f(ans, self._fenwick_tree[i])
            i += 1
            length -= (1 << max_p2)

        return ans

    def query(self, l, r): 
        ans = self._query_helper(r)
        if l > 0:
            ans = self._inv_f(ans, self._query_helper(l - 1))

        return ans
    

class SegmentTreeIdemponent:
    
    def __init__(self, arr, f):
        self._f = f
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        
        # Build the tree
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self._f(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, idx, value):
        idx += self.n  # Move to leaf node
        self.tree[idx] = value  # Update value
        while idx > 1:
            idx //= 2
            self.tree[idx] = self._f(self.tree[2 * idx], self.tree[2 * idx + 1])

    def query(self, l, r):
        l += self.n  # Convert to leaf index
        r += self.n  # Convert to leaf index
        best = None

        while l <= r:
            if l % 2 == 1:  # If `l` is a right child
                if best == None:
                    best = self.tree[l]
                best = self._f(best, self.tree[l])
                l += 1
            if r % 2 == 0:  # If `r` is a left child
                if best == None:
                    best = self.tree[r]
                best = self._f(best, self.tree[r])
                r -= 1
            l //= 2
            r //= 2

        return best
    

def clz(x):  # similar to __builtin_clz(x) in cpp
    # Count Left Zeros
    if x == 0:
        return 32  # or return 64 if treating as a 64-bit integer
    return 32 - x.bit_length()

    # # Example
    # x = 16  # Binary: 00000000 00000000 00000000 00010000
    # print(clz(x))  # Output: 27

def ctz(x):  # similar to __builtin_ctz(x) in cpp
    # Count Trailing Zeros
    if x == 0:
        return 32  # or return 64 for 64-bit numbers
    return (x & -x).bit_length() - 1

    # # Example
    # x = 16  # Binary: 10000
    # print(ctz(x))  # Output: 4

def pop_count(x):  # similar to __builtin_popcount(x) in cpp
    return bin(x).count('1')

    

# primes = soe(1, 5890000)
# facs = [1]
# for num in range(1, 2*int(1e5) + 2):
#     facs.append((facs[-1] * num) % MOD)


################################# TREAP #########################################################
import random

class Node:
    def __init__(self, val):
        self.val = val
        self.pri = random.randint(1, 1 << 30)
        self.left = None
        self.right = None
        self.size = 1
        self.sum = val

def size(t):
    return t.size if t else 0

def getsum(t):
    return t.sum if t else 0

def update(t):
    if not t: return
    t.size = 1 + size(t.left) + size(t.right)
    t.sum = t.val + getsum(t.left) + getsum(t.right)

def split(t, k):
    if not t:
        return (None, None)
    if size(t.left) >= k:
        left, right = split(t.left, k)
        t.left = right
        update(t)
        return (left, t)
    else:
        left, right = split(t.right, k - size(t.left) - 1)
        t.right = left
        update(t)
        return (t, right)

def merge(a, b):
    if not a or not b:
        return a or b
    if a.pri > b.pri:
        a.right = merge(a.right, b)
        update(a)
        return a
    else:
        b.left = merge(a, b.left)
        update(b)
        return b


class ImplicitTreap:
    def __init__(self):
        self.root = None

    def insert(self, index, val):
        new_node = Node(val)
        left, right = split(self.root, index)
        merged = merge(left, new_node)
        self.root = merge(merged, right)

    def delete(self, index):
        left, right = split(self.root, index)
        mid, right = split(right, 1)
        self.root = merge(left, right)

    def update(self, index, val):
        self.delete(index)
        self.insert(index, val)

    def query(self, l, r):
        left, mid = split(self.root, l)
        mid, right = split(mid, r - l + 1)
        ans = getsum(mid)
        self.root = merge(left, merge(mid, right))
        return ans

    def inorder(self):
        res = []
        def dfs(t):
            if not t: return
            dfs(t.left)
            res.append(t.val)
            dfs(t.right)
        dfs(self.root)
        return res
    
##################################################################################

################### SegmentTree Updates ranges ####################################
class SegmentTreeRangeUpdate:
    def __init__(self, size):
        self.N = size
        self.tree = [0] * (2 * self.N)
        self.lazy = [0] * self.N  # only need lazy for internal nodes

    def _apply(self, i, value, k):
        self.tree[i] += value * k
        if i < self.N:
            self.lazy[i] += value

    def _push(self, l, r):
        h = self.N.bit_length()
        for s in range(h, 0, -1):
            for i in ((l >> s), (r >> s)):
                if self.lazy[i]:
                    self._apply(i << 1, self.lazy[i], 1 << (s - 1))
                    self._apply(i << 1 | 1, self.lazy[i], 1 << (s - 1))
                    self.lazy[i] = 0

    def _build(self, l, r):
        l0, r0 = l, r
        while l > 1:
            l >>= 1
            self.tree[l] = self.tree[l << 1] + self.tree[l << 1 | 1] + self.lazy[l] * (r0 - l0)
        while r > 1:
            r >>= 1
            self.tree[r] = self.tree[r << 1] + self.tree[r << 1 | 1] + self.lazy[r] * (r0 - l0)

    def range_add(self, l, r, value):
        """Add value to interval [l, r)"""
        l += self.N
        r += self.N
        l0, r0 = l, r
        self._push(l0, r0 - 1)

        k = 1
        while l < r:
            if l & 1:
                self._apply(l, value, k)
                l += 1
            if r & 1:
                r -= 1
                self._apply(r, value, k)
            l >>= 1
            r >>= 1
            k <<= 1

        self._build(l0, r0 - 1)

    def range_sum(self, l, r):
        """Query sum in interval [l, r)"""
        l += self.N
        r += self.N
        self._push(l, r - 1)

        res = 0
        while l < r:
            if l & 1:
                res += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                res += self.tree[r]
            l >>= 1
            r >>= 1
        return res


####################################################


######################## Wavelet Tree ####################################
class WaveletTree:
    def __init__(self, data, min_val, max_val):
        self.lo = min_val
        self.hi = max_val
        self.b = [0]  # prefix sum of left child
        self.left = self.right = None

        if self.lo == self.hi or not data:
            return

        mid = (self.lo + self.hi) // 2
        left_part = []
        right_part = []

        for val in data:
            if val <= mid:
                left_part.append(val)
                self.b.append(self.b[-1] + 1)
            else:
                right_part.append(val)
                self.b.append(self.b[-1])
        
        self.left = WaveletTree(left_part, self.lo, mid)
        self.right = WaveletTree(right_part, mid + 1, self.hi)

    def count_leq(self, l, r, x):
        """Count numbers ≤ x in [l, r]"""
        if l > r or x < self.lo:
            return 0
        if self.hi <= x:
            return r - l + 1
        lcnt = self.b[l]
        rcnt = self.b[r + 1]
        return self.left.count_leq(lcnt, rcnt - 1, x) + self.right.count_leq(l - lcnt, r - rcnt, x)

    def kth(self, l, r, k):
        """Find k-th smallest in [l, r]"""
        if l > r:
            return -1  # invalid
        if self.lo == self.hi:
            return self.lo
        inLeft = self.b[r + 1] - self.b[l]
        if k <= inLeft:
            return self.left.kth(self.b[l], self.b[r + 1] - 1, k)
        else:
            return self.right.kth(l - self.b[l], r - self.b[r + 1] + 1, k - inLeft)

##########################################################

class Heap:
    def __init__(self, is_min_heap=True):
        self.data = []  # list of (value, id)
        self.is_min = is_min_heap

    def compare(self, a, b):
        return a < b if self.is_min else a > b

    def push(self, value):
        self.data.append(value)
        self._sift_up(len(self.data) - 1)

    def top(self):
        return self.data[0] if self.data else None

    def pop(self):
        if not self.data:
            return None
        self._swap(0, len(self.data) - 1)
        val = self.data.pop()
        self._sift_down(0)
        return val

    def _sift_up(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.compare(self.data[i][0], self.data[parent][0]):
            self._swap(i, parent)
            i = parent
            parent = (i - 1) // 2

    def _sift_down(self, i):
        n = len(self.data)
        while True:
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and self.compare(self.data[left][0], self.data[smallest][0]):
                smallest = left
            if right < n and self.compare(self.data[right][0], self.data[smallest][0]):
                smallest = right
            if smallest == i:
                break
            self._swap(i, smallest)
            i = smallest

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def is_empty(self):
        return len(self.data) == 0

class DualPriorityQueue:
    def __init__(self):
        self.min_heap = Heap(is_min_heap=True)
        self.max_heap = Heap(is_min_heap=False)
        self.valid = set()  # active unique ids
        self.counter = 0    # unique id per insertion

    def insert(self, value):
        
        uid = self.counter
        self.min_heap.push((value, uid))
        self.max_heap.push((value, uid))
        self.valid.add(uid)
        self.counter += 1

    def _clean(self, heap):
        while not heap.is_empty():
            val, uid = heap.top()
            if uid in self.valid:
                return val, uid
            heap.pop()  # discard invalid
        return None

    def pop_min(self):
        item = self._clean(self.min_heap)
        if item:
            val, uid = self.min_heap.pop()
            self.valid.remove(uid)
            return val, uid
        return None

    def pop_max(self):
        item = self._clean(self.max_heap)
        if item:
            val, uid = self.max_heap.pop()
            self.valid.remove(uid)
            return val, uid
        return None

    def get_min(self):
        return self._clean(self.min_heap)

    def get_max(self):
        return self._clean(self.max_heap)

    def is_empty(self):
        return len(self.valid) == 0



def get_connected_components(adj_list):
    n = len(adj_list)
    visited = [False] * n
    components = []

    for start in range(n):
        if not visited[start]:
            stack = [start]
            component = []
            visited[start] = True

            while stack:
                node = stack.pop()
                component.append(node)
                for neighbor in adj_list[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)

            components.append(component)

    return components


class DSU:
	def __init__(self, size: int) -> None:
		self.parents = [i for i in range(size)]
		self.sizes = [1 for _ in range(size)]

	def find(self, x: int) -> int:
		""":return: the "representative" node in x's component"""
		if self.parents[x] == x:
			return x
		self.parents[x] = self.find(self.parents[x])
		return self.parents[x]

	def unite(self, x: int, y: int) -> bool:
		""":return: whether the merge changed connectivity"""
		x_root = self.find(x)
		y_root = self.find(y)
		if x_root == y_root:
			return False

		if self.sizes[x_root] < self.sizes[y_root]:
			x_root, y_root = y_root, x_root

		self.parents[y_root] = x_root
		self.sizes[x_root] += self.sizes[y_root]
		return True

	def connected(self, x: int, y: int) -> bool:
		""":return: whether x and y are in the same connected component"""
		return self.find(x) == self.find(y)


def minSwaps(a, b):
    
    # Store index of elements in 'a'
    pos = [0] * (len(a) + 1)
    for i in range(len(a)):
        pos[a[i]] = i

    swaps = 0
    i = 0
    n = len(a)

    while i < n:
        
        # If element is not in the correct position, swap it
        if a[i] != b[i]:
            swap_idx = pos[b[i]]

            # Swap elements in 'b'
            b[i], b[swap_idx] = b[swap_idx], b[i]
            swaps += 1

            # Re-evaluate current index to check correctness
            i -= 1
        
        i += 1

    return swaps


def is_perfect_square(num):
    sq = math.isqrt(num)
    return (sq * sq) == num
    

def lsb(num):
    if num == 0:
        return 0
    return (num & -num).bit_length() - 1


def msb(num):
    if num == 0:
        return 0
    return num.bit_length() - 1

def is_sum_law(n):
    if n < 0:
        return False
    if n == 0:
        return True
    
    # Solve x(x + 1)/2 = n => x^2 + x - 2n = 0
    discriminant = 1 + 8 * n
    sqrt_d = int(math.isqrt(discriminant))
    
    # Check if discriminant is a perfect square
    if sqrt_d * sqrt_d != discriminant:
        return False
    
    # Check if (-1 + sqrt_d) is divisible by 2
    x = (-1 + sqrt_d)
    return x % 2 == 0

def count_children(adj, parents):
    num_children = [-1] * len(adj)
    def calc_num_children(node):
        ans = 0
        if num_children[node] != -1: return num_children[node]
        for child in adj[node]:
            if child != parents[child]:
                ans += (1 + calc_num_children(child))

        num_children[node] = ans
        return ans
    
    calc_num_children(0)
    return num_children


####################################### Binary Lifting ########################################################
class Binary_Lifting:

    def __init__(self, adj):
        n = len(adj) - 1
        self.mat = [[0 for _ in range(25)] for _ in range(n + 1)]
        self.depth = [0] * (n + 1)
        stack = [1]
        self.depth[1] = 1
        vis = [0] * (n + 1)
        vis[1] = 1
        while stack:
            cur = stack.pop()
            for ch in adj[cur]:
                if not vis[ch]:
                    vis[ch] = 1
                    stack.append(ch)
                    self.mat[ch][0] = cur
                    self.depth[ch] = self.depth[cur] + 1

        # print("depth in build", self.depth)
        for level in range(1, 25):
            for node in range(1, n + 1):
                self.mat[node][level] = self.mat[self.mat[node][level - 1]][level - 1]

    def move(self, node, k):
        for level in range(25 - 1, -1, -1):
            if k & (1 << level):
                node = self.mat[node][level]

        return node



    def lca(self, a, b):
        if self.depth[a] < self.depth[b]:
            a, b = b, a

        a = self.move(a, self.depth[a] - self.depth[b])
        if a == b: return a
        # print("after move", a, b)
        for level in range(25 - 1, -1, -1):
            if self.mat[a][level] != self.mat[b][level]:
                a = self.mat[a][level]
                b = self.mat[b][level]
                
        # print("debug", a, b)
        return self.mat[a][0]
        
        



###############################################################################################################


def countSubarraysEqualsK(arr, k):
    # Dictionary to store prefix sums frequencies
    prefixSums = {}
    res = 0
    currSum = 0

    for val in arr:
        # Add current element to sum so far
        currSum += val

        # If currSum is equal to desired sum, then a new subarray is found
        if currSum == k:
            res += 1

        # Check if the difference exists in the prefixSums dictionary
        if currSum - k in prefixSums:
            res += prefixSums[currSum - k]

        # Add currSum to the dictionary of prefix sums
        prefixSums[currSum] = prefixSums.get(currSum, 0) + 1

    return res


def same_digits_same_pos(n1, n2):
    n1 = str(n1)
    n2 = str(n2)
    ans = 0
    for i in range(len(n1)):
        ans += (n1[i] == n2[i])

    return ans




########################################################################################
class TreeDistance:
    def __init__(self, n):
        self.n = n
        self.LOG = (n).bit_length()
        self.graph = [[] for _ in range(n)]
        self.up = [[-1] * self.LOG for _ in range(n)]
        self.depth = [0] * n

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, u, parent):
        self.up[u][0] = parent
        for i in range(1, self.LOG):
            if self.up[u][i - 1] != -1:
                self.up[u][i] = self.up[self.up[u][i - 1]][i - 1]

        for v in self.graph[u]:
            if v != parent:
                self.depth[v] = self.depth[u] + 1
                self.dfs(v, u)

    def build(self, root=0):
        self.dfs(root, -1)

    def lca(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        for i in reversed(range(self.LOG)):
            if self.up[u][i] != -1 and self.depth[self.up[u][i]] >= self.depth[v]:
                u = self.up[u][i]
        if u == v:
            return u
        for i in reversed(range(self.LOG)):
            if self.up[u][i] != -1 and self.up[u][i] != self.up[v][i]:
                u = self.up[u][i]
                v = self.up[v][i]
        return self.up[u][0]

    def distance(self, u, v):
        lca_node = self.lca(u, v)
        return self.depth[u] + self.depth[v] - 2 * self.depth[lca_node]

########################################################################################

from collections import deque

def find_tree_diameter_ends(n, adj):
    """
    Returns the two endpoints of the diameter of the tree.
    
    Parameters:
        n    : number of nodes (0-indexed)
        adj  : adjacency list of the tree

    Returns:
        (u, v): tuple of nodes representing the two ends of the diameter
    """

    def bfs(start):
        dist = [-1] * n
        dist[start] = 0
        q = deque([start])
        farthest = start
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
                    if dist[v] > dist[farthest]:
                        farthest = v
        return farthest, dist

    # First BFS from any node (0) to get one end of the diameter
    u, _ = bfs(0)

    # Second BFS from u to get the farthest node from it
    v, dist_u = bfs(u)

    # v is the other end of the diameter
    return u, v

def is_valid_brackets(st):
    stack = []
    for i in range(len(st)):
        if st[i] == "(":
            stack.append("(")
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
            
    return not stack


# MOD = 1000000353

def precomp_facts(mx):
    # MOD = 998244353
    MAX = mx  # slightly more than max a, b, k

    fac = [1] * MAX
    inv_fac = [1] * MAX

    for i in range(1, MAX):
        fac[i] = fac[i - 1] * i % MOD

    inv_fac[MAX - 1] = pow(fac[MAX - 1], MOD - 2, MOD)
    for i in range(MAX - 2, -1, -1):
        inv_fac[i] = inv_fac[i + 1] * (i + 1) % MOD

    return fac, inv_fac
    

# def C(n, k):
#     if k < 0 or k > n:
#         return 0
    
#     return fac[n] * inv_fac[k] % MOD * inv_fac[n - k] % MOD


# def lucas(n, k):
#     if k == 0:
#         return 1
#     return lucas(n // MOD, k // MOD) * C(n % MOD, k % MOD) % MOD

# def nCrModpDP(n, r, p):
    
#     # The array C is going to store
#     # last row of pascal triangle
#     # at the end. And last entry 
#     # of last row is nCr
#     C = [0] * (n + 1)

#     # Top row of Pascal Triangle
#     C[0] = 1

#     # One by constructs remaining 
#     # rows of Pascal Triangle from 
#     # top to bottom
#     for i in range(1, (n + 1)):
        
#         # Fill entries of current 
#         # row using previous row
#         # values
#         j = min(i, r); 
#         while(j > 0):
#             C[j] = (C[j] + C[j - 1]) % p
#             j -= 1
#     return C[r]


# def nCrModpLucas(n, r, p):
    
#     # Base case
#     if (r == 0):
#         return 1
        
#     # Compute last digits of n
#     # and r in base p
#     ni = int(n % p)
#     ri = int(r % p)
        
#     # Compute result for last digits 
#     # computed above, and for remaining 
#     # digits. Multiply the two results 
#     # and compute the result of 
#     # multiplication in modulo p.
#     # Last digits of n and r
#     return (nCrModpLucas(int(n / p), int(r / p), p) * 
#             nCrModpDP(ni, ri, p)) % p; # Remaining digits


# primes = soe(1, 1000007)
# fac, inv_fac = precomp_facts(1000007)



class DoubleHashedString:
    M1 = 10**9 + 7
    M2 = 10**9 + 9
    B1 = random.randint(256, 10000)
    B2 = random.randint(256, 10000)

    _pow1 = [1]
    _pow2 = [1]

    def __init__(self, s: str):
        while len(self._pow1) <= len(s):
            self._pow1.append((self._pow1[-1] * self.B1) % self.M1)
            self._pow2.append((self._pow2[-1] * self.B2) % self.M2)

        self._hash1 = [0] * (len(s) + 1)
        self._hash2 = [0] * (len(s) + 1)

        for i in range(len(s)):
            self._hash1[i + 1] = (self._hash1[i] * self.B1 + ord(s[i])) % self.M1
            self._hash2[i + 1] = (self._hash2[i] * self.B2 + ord(s[i])) % self.M2

    def get_hash(self, start: int, end: int):
        """Returns a tuple (hash1, hash2) for s[start:end+1]"""
        len_seg = end - start + 1

        raw1 = (self._hash1[end + 1] - self._hash1[start] * self._pow1[len_seg]) % self.M1
        raw2 = (self._hash2[end + 1] - self._hash2[start] * self._pow2[len_seg]) % self.M2

        return (raw1, raw2)



class DoubleAnagramHasher:
    M1 = 10**9 + 7
    M2 = 10**9 + 9
    B1 = random.randint(256, 10000)
    B2 = random.randint(256, 10000)

    def __init__(self, s: str):
        self.n = len(s)
        self.prefix_freq = [[0] * 26 for _ in range(self.n + 1)]

        for i in range(self.n):
            for j in range(26):
                self.prefix_freq[i + 1][j] = self.prefix_freq[i][j]

            c = s[i].lower()
            if 'a' <= c <= 'z':
                self.prefix_freq[i + 1][ord(c) - ord('a')] += 1

    def get_hash(self, l: int, r: int):
        """Returns a double hash for the multiset (anagram) in s[l:r+1]"""
        freq = [self.prefix_freq[r + 1][i] - self.prefix_freq[l][i] for i in range(26)]

        h1 = 0
        h2 = 0
        for count in freq:
            h1 = (h1 * self.B1 + count) % self.M1
            h2 = (h2 * self.B2 + count) % self.M2

        return (h1, h2)



class RollingHasher:
    def __init__(self, base=None, mod=10**9+7):
        self.mod = mod
        self.base = base if base is not None else random.randint(256, 10000)
        self.pow = [1]
    
    def extend_pow(self, n):
        while len(self.pow) <= n:
            self.pow.append((self.pow[-1] * self.base) % self.mod)

    def build(self, s):
        self.extend_pow(len(s))
        prefix = [0] * (len(s) + 1)
        for i in range(len(s)):
            prefix[i+1] = (prefix[i] * self.base + ord(s[i])) % self.mod
        return prefix

    def get_hash(self, prefix, l, r):
        length = r - l + 1
        return (prefix[r+1] - prefix[l] * self.pow[length]) % self.mod



def xor_hashing(arr, hash_vals):
    
    prx_zor = []
    cur_zor = 0
    unique = set()
    for num in arr:
        if str(num) not in unique:
            cur_zor ^= hash_vals[str(num)]
            unique.add(str(num))

        prx_zor.append(cur_zor)

    return prx_zor


def solve(file=False, infile=None, outfile=None):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    
    #######################################################################################
    #######################################################################################
    ################################ Start Core Code ######################################
    #######################################################################################
    #######################################################################################
    
    n = read_int(infile=infile)
    # n, c = read_numbers(infile=infile)
    a = read_numbers()
    # a = read_str().split()
    # b = read_numbers()
    # m = read_int()
    # s = read_str(infile=infile)
    # t = read_str(infile=infile)
    # adj = [[] for _ in range(n)]
    # parents = [-1] * n
    # c = [-1] * n
    # edges = []
    # root = None
    prx = prefix_min(a)
    for i in range(1, n):
        diff = a[i] - prx[i - 1]
        if a[i] > prx[i - 1] and (diff >= prx[i - 1]):
            print("NO")
            return

    print("YES")
                
        


    



    #######################################################################################
    #######################################################################################
    ################################ End Core Code ########################################
    #######################################################################################
    #######################################################################################

      




use_file = False
if use_file:

    # -------------- For File input output Questions --------------
    file = "censor"
    with open(f"{file}.in", "r") as infile, open(f"{file}.out", "w") as outfile:
        t = 1
        # t = read_int(infile=infile)
        for _ in range(t):
            solve(file=True, infile=infile, outfile=outfile)
            # threading.Thread(target=solve).start()
    

else:
    # m = 3
    # rad = 7
    # PI = math.acos(-1)
    # for circle in range(1, 10):
    #     print(circle, rad + m * (circle - 1), 2*PI*rad*circle + 2*PI*m*(((circle - 1) * circle)//2))
    t = 1
    t = read_int()
    for _ in range(t):
        solve()
        # threading.Thread(target=solve).start()


