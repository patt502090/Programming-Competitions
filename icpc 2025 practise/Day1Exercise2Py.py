ck = 0
try:
    while True:
        n = input().split()
        for i in n:
            if i.count("e") or i.count("E"):
                ck += 1
except BaseException:
    print(ck)
    pass
