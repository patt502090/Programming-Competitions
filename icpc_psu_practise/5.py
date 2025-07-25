lst = list(map(int,input()))
lst.sort()
lst = [x for x in lst if x != 0]
print("".join(map(str,lst)))