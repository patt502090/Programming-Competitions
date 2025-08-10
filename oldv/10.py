count = 0
while True:
    n = input()
    for i in n:
        if i.isupper():
            count += 1
    if n == "#":
        break
print(count)
