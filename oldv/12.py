import sys
import string


def EOF():
    for _ in sys.stdin:
        yield _


def palin(word):
    wordR = word.strip(string.punctuation)
    # print(wordR)
    return wordR == wordR[::-1]


def check(line):
    C = []
    words = line.split()
    for word in words:
        word = word.lower()
        if len(word) == 1:
            continue
        if palin(word):
            C.append(word.strip(string.punctuation))
    return C


all = []
for line in EOF():
    if str(line) == "#":
        break
    if len(check(line)) > 0:
        word = check(line)
        all.extend(word)

all.sort()
print(len(all), end=" ")
for i in all:
    print(i, end=" ")
