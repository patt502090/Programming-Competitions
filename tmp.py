# print(list(map(sum,zip(*cnt))))
# print("YES" if sum(map(sum,zip(*cnt))) == 0 else "NO")


# print("YES" if sum(cnt) == 0 else "NO")

# A. Arrival of the General (NinePon)
# def solve():
#     n = II()
#     lst = LII()
#     cnt = 0
#     mx = max(lst)
#     mn = min(lst)
#     i = 0
        
#     for i in range(n):
#         if lst[i] == mx:
#             while i > 0:
#                 lst[i],lst[i-1] = lst[i-1],lst[i]
#                 cnt += 1
#                 i -= 1
#             break
#     for i in range(n-1,-1,-1):
#         if lst[i] == mn:
#             while i <= n - 1:
#                 lst[i],lst[i+1] = lst[i+1],lst[i]
#                 i += 1
#                 cnt += 1
#             break        

#     print(cnt)  

# " WUBIWEBAM to "I AM" "
# print(' '.join(word.replace("WUB"," ").split()))

#  n = II()
#     v = sorted(LII())
#     l, r, x = 0, 2000000, -1
    
#     while l <= r:
#         rich = l + (r - l) // 2
#         b = v[:]  
#         b[-1] += rich
#         total_sum = sum(b)
#         avg_wealth = total_sum / n
#         counter = 0
#         for wealth in b:
#             if wealth < avg_wealth / 2.0:
#                 counter += 1
#         if counter > n // 2:
#             x = rich
#             r = rich - 1
#         else:
#             l = rich + 1
            
#     print(x)


    # n = II()
    # lst = sorted(LII(),reverse = True)
    # cnt = 0
    # ck = 0
    # for i in range(len(lst)):   
    #     if lst[i] > 2 and ck == 0 and lst[i] <= 4:
    #         cnt += 1
    #     else:
    #         ck == lst[i]
    #         if lst[i] + ck > 3 and ck:
    #             cnt += 1
    #             ck = 0
    #         else:
    #             ck += lst[i]
            
            
    # print(cnt)
            

# def solve():
#     n = II()
#     lst = LII()
#     count = 0
#     ckMax = float('-inf')
    
#     count1 = 0
#     ckMax1 = float('-inf')
    
#     for i in range(0, n, 2):
#         ckMax = max(ckMax,lst[i])
#         count += 1
#     for i in range(1, n, 2):
#         ckMax1 = max(ckMax1,lst[i])
#         count1 += 1
    
#     print(max(count + ckMax, count1 + ckMax1))


def remove_duplicates(lst):
    seen = set()
    result = []

    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)

    return result

