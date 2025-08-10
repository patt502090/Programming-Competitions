for _ in range(int(input())):
    n = int(input())
    a = (input())
    a = a.lower()
    b = ''
    i = 0
    while i < n:
        j = i
        b += a[i]
        while j < n:
            if a[j] != a[i]:
                break
            else:
                j += 1
        i = j
    if b == 'meow':
        print("YES")
    else:
        print("NO")
