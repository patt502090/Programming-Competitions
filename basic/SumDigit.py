def solve():
    n = input()
    lst_num = [str(x) for x in n]
    print(int(lst_num[0]) + int(lst_num[1]))


for _ in range(int(input())):
    solve()
