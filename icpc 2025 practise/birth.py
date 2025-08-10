def solve():
    lst = []
    while True:
        try:
            line = input()
            if line.strip() == "":
                break
            name, day, month, year = line.split()
            lst.append((int(year), int(month), int(day), name))
        except EOFError:
            break

    if lst:
        lst.sort()
        youngest = lst[-1][3]
        oldest = lst[0][3]
        print(f"{youngest}\n{oldest}")


if __name__ == "__main__":
    TEST = 1
    for _ in range(TEST):
        solve()
