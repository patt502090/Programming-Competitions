import sys

n = int(sys.stdin.readline())
print(n)
for i in range(1, n + 1):
    print(i, i)
sys.stdout.flush()

W = int(sys.stdin.readline())

S = n * (n + 1) // 2
expected = 500 * S
diff = W - expected
print(f"! {diff}")
sys.stdout.flush()
