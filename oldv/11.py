import sys
def EOF():
    for line in sys.stdin:
        yield line

for line in EOF():
    if line == "#":
        print("#")
        break
    else :
        print(line.strip()[::-1])

