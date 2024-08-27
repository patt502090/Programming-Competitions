def solve():
    n = int(input())
    lst = [int(x) for x in input().split()]
    loop = int(input())
    
    for _ in range(loop):
        word = input()
        
        if len(word) != n:
            print("No")
            continue
        
        num_to_char = {}
        char_to_num = {}
        is_valid = True

        for num, char in zip(lst, word):
            if num in num_to_char:
                if num_to_char[num] != char:
                    is_valid = False
                    break
            else:
                num_to_char[num] = char
                
            if char in char_to_num:
                if char_to_num[char] != num:
                    is_valid = False
                    break
            else:
                char_to_num[char] = num
                
        print("1::",num_to_char)
        print("2::",char_to_num)
        if is_valid:
            print("YES")
        else:
            print("No")


for _ in range(int(input())):
    solve()
