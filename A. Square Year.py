import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def is_square_year(s):
    year = int(s)
    root = int(year ** 0.5)

    if root * root != year:
        return -1
    
    for a in range(0, root + 1):
        b = root - a
        if (a + b) ** 2 == year:
            return f"{a} {b}"
    
    return -1

def main():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        print(is_square_year(s))

if __name__ == '__main__':
    main()
