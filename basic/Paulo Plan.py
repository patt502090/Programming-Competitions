S = [str(x) for x in input()]
T = [str(x) for x in input()]
count_S = 0
count_T = 0

for j in range(len(S)):
    for k in range(j+1,len(S)):
        if S[j] > S[k]:
            count_S += 1
            S[j],S[k] = S[k],S[j]
        else:
            continue


for j in range(len(T)):
    for k in range(j+1,len(T)):
        if T[j] < T[k]:
            count_T += 1
            T[j],T[k] = T[k],T[j]
        else:
            continue

print(count_S,count_T)
print(T)
print(S)

