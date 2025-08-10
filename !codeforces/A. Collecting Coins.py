import os
import io
import sys

data = io.BytesIO(os.read(0, os.fstat(0).st_size)
                  ).read().decode().strip().split('\n')

if not data or data[0] == '':
    print("No input detected")
    sys.exit()

write = sys.stdout.write

T = int(data[0])
res = []

for i in range(1, T + 1):
    a, b, c, n = map(int, data[i].split())
    mx = max(a, b, c)
    need = 3 * mx - (a + b + c)
    res.append("YES\n" if n >= need and (n - need) % 3 == 0 else "NO\n")

write(''.join(res))
