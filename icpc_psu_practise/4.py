lst = list(map(int, input()))
lst.sort(reverse=True)
print("".join(map(str, lst)))
