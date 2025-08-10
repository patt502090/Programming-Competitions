def check(lst):
    ans = []
    char_map = {
        '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']
    }

    key = lst[0]
    is_long_key = key in ['7', '9']
    length = len(lst)
    full_set_count = length // (4 if is_long_key else 3)
    remain = length % (4 if is_long_key else 3)

    if key != '1':
        if remain:
            ans.append(char_map[key][remain - 1])
        ans.extend([char_map[key][-1]] * full_set_count)

    return ''.join(ans)


def solve():
    num, ck = I(), []
    for i in range(len(num)):
        ck.append(num[i])
        if i == len(num) - 1 or num[i] != num[i + 1]:
            print(check(ck), end='')
            ck = []


if __name__ == '__main__':
    for _ in range(1):
        solve()
