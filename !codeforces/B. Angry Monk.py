def solve():
    n, k = map(int,input().split())
    num = [int(x) for x in input().split()]
    i = count = 0
    num.sort(reverse = True)
    while len(num) > 1:
        if num[i] >= 2:
            j = i + 1
            while j < len(num):
                if num[j] == 1:
                    num.pop(j)
                    num[i] += 1
                    count += 1
                elif num[j] >= 2:
                    num[j] -= 1
                    num.append(1)
                    count += 1
                print(num)
            j += 1
        i += 1

    print(num)
    print(count)
for _ in range(int(input())):
    solve()
