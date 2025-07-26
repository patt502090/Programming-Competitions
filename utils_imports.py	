# common_imports.py
"""
ไฟล์นี้เก็บชุด import ที่ใช้บ่อยในโปรเจกต์ Python
เพื่อให้เราเขียนโค้ดสะดวกและรวดเร็วขึ้น

สามารถ import ทั้งหมด หรือ import เฉพาะ module ที่ต้องการ
จากไฟล์นี้ได้เลย

---

ตัวอย่างการใช้งาน (ในไฟล์อื่น ๆ):
from common_imports import *
# หรือ
from common_imports import deque, Counter

"""

# --------- โมดูลระบบและไฟล์ ---------
import os                      # จัดการไฟล์, โฟลเดอร์, environment variables, รันคำสั่ง shell
import sys                     # ควบคุม input/output, arguments, ตั้ง recursion limit
from sys import stdin, stdout, setrecursionlimit  
# stdin, stdout: อ่านเขียนข้อมูลเร็ว (แทน input() / print())
# setrecursionlimit: ปรับความลึกของ recursive calls

# --------- โมดูลสุ่ม ---------
import random                  # สุ่มตัวเลข, เลือก item, สับ list
from random import randint, choice, shuffle  
# randint: สุ่มเลขจำนวนเต็มในช่วงที่กำหนด
# choice: เลือก element แบบสุ่มจาก sequence
# shuffle: สลับตำแหน่งใน list แบบสุ่ม

# --------- โมดูลคัดลอกและเลขทศนิยม ---------
from copy import deepcopy      # คัดลอกแบบลึก (deep copy) ไม่อ้างอิง object เดิม
from decimal import Decimal, getcontext  
# Decimal: คำนวณเลขทศนิยมแม่นยำ
# getcontext: กำหนดความแม่นยำการคำนวณ Decimal

# --------- โมดูลตรวจสอบประเภทข้อมูล ---------
from types import GeneratorType  
# ใช้เช็กว่า object เป็น generator หรือไม่

# --------- โมดูลฟังก์ชันช่วยและคำนวณ ---------
from functools import lru_cache, reduce  
# lru_cache: จำผลลัพธ์ฟังก์ชันเพื่อลดการคำนวณซ้ำ (memoization)
# reduce: รวมค่าจาก iterable ด้วยฟังก์ชันที่กำหนด

# --------- โมดูล binary search ---------
from bisect import bisect_left, bisect_right  
# bisect_left: หาตำแหน่งแทรกซ้ายใน sorted list
# bisect_right: หาตำแหน่งแทรกขวาใน sorted list

# --------- โมดูลโครงสร้างข้อมูลและนับจำนวน ---------
from collections import Counter, defaultdict, deque  
# Counter: นับจำนวน element ใน iterable
# defaultdict: dict ที่กำหนด default value ให้ key ใหม่
# deque: queue แบบเพิ่ม/ลบหน้าหลังได้เร็ว (O(1))

# --------- โมดูลจัดการ iterator และชุดข้อมูล ---------
from itertools import accumulate, combinations, permutations  
# accumulate: ผลรวมสะสมใน iterable
# combinations: สร้างชุดย่อยแบบไม่เรียงลำดับ
# permutations: สร้างชุดย่อยแบบเรียงลำดับ

# --------- โมดูล heap (priority queue) ---------
from heapq import heapify, heappop, heappush, heappushpop  
# heapify: สร้าง heap จาก list
# heappop: ดึงค่าที่น้อยสุดออกจาก heap
# heappush: ใส่ค่าลง heap
# heappushpop: ใส่ค่าแล้วดึงค่าที่น้อยที่สุดออกในขั้นตอนเดียว

# --------- โมดูลช่วยเขียน type hint ---------
from typing import Generic, Iterable, Iterator, TypeVar, Union, List  
# ใช้กำหนดชนิดตัวแปรและพารามิเตอร์ในฟังก์ชัน หรือ class

# --------- โมดูลจัดการชุดตัวอักษรและสัญลักษณ์ ---------
from string import ascii_lowercase, ascii_uppercase, digits, punctuation, printable, whitespace
# ascii_lowercase: ตัวอักษร a-z
# ascii_uppercase: ตัวอักษร A-Z
# digits: ตัวเลข 0-9
# punctuation: เครื่องหมายวรรคตอน (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
# printable: ตัวอักษรทั้งหมดที่พิมพ์ได้ (รวมช่องว่าง, ตัวเลข, สัญลักษณ์)
# whitespace: ช่องว่าง เช่น space, tab, newline

# --------- โมดูลคณิตศาสตร์ ---------
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
# ceil: ปัดขึ้น (เช่น 3.2 → 4)
# floor: ปัดลง (เช่น 3.8 → 3)
# sqrt: รากที่สอง
# pi: ค่า π (3.1415...)
# factorial: แฟกทอเรียล n!
# gcd: หาตัวหารร่วมมากที่สุด (Greatest Common Divisor)
# log, log10, log2: ลอการิทึมฐาน e, 10, 2
# inf: ค่าคงที่อนันต์ (∞)
