word = [str(x) for x in str(input())]
Upper = 0
Lower = 0
for i in word:
    if i.isupper():
        Upper += 1
    elif i.islower():
        Lower += 1
if Upper > Lower:
    print(''.join(word).upper())
else :
    print(''.join(word).lower())

