import sys
from string import ascii_lowercase, ascii_uppercase, digits
data = ""

try:
    while True:
        n = input()
        data += n
except EOFError:
    pass

# n = int(data[0])

# data = list(map(int, data[1:n+1]))
print(data)
cnt = 0
for i in data:
    if i in digits:
        cnt += 1
print(cnt)