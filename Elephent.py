n = int(input())
if n - 5 <= 0:
    print("1")
    exit();
num = [5,4,3,2,1]
count = 0
while n > 0:
    for i in num:
        k = n//i
        if k > 0:
            n -= i*k
            count += k
        elif n <= 0:
            break
print(count)




