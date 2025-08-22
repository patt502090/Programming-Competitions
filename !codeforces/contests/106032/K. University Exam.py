pati = int(input())
if pati >= 18:
    tit = int(input())
else:
    print("Failed")
    exit()
print("Passed" if pati >= 18 and pati + tit >= 60 else "Failed")
