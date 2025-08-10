lst = sorted(map(int, input()))
lst = [x for x in lst if x != 0]
print("".join(map(str, lst)))
