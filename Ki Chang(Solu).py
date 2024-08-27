import math
N, M, H, Q = map(int, input().split())
distance = [list(map(int, input().split())) for _ in range(N)]
net = list(map(int, input().split()))
quest = [list(map(int, input().split())) for _ in range(Q)]

for q in quest:
    ans = 0
    count_x = 0
    c = distance.copy()
    n = net.copy()
    ch = True

    if q[0] == len(distance):
        c.sort(reverse=True, key=lambda x: x[0] + x[1])
        n.sort(reverse=True)
    else:
        c.sort(key=lambda x: x[1])
        n.sort()

    for i in range(q[0]):
        if c[i][1] - H > n[i]:
            print("-1")
            ch = False
            break
        else:
            found = False
            for net_value in n:
                if c[i][1] - H <= net_value:
                    found = True
                    n.remove(net_value)
                    break
            if found:
                count_x = c[i][0]

    if ch:
        print(count_x)
