from collections import Counter
from string import ascii_letters

worda = ""
try:
    while True:
        word = input()
        worda += word
except EOFError:
    pass

filtered = [ch.upper() for ch in worda if ch in ascii_letters]

x = Counter(filtered)

x = sorted(x.items(), key=lambda item: (-item[1], item[0]))

for ch, count in x:
    print(ch, count)
