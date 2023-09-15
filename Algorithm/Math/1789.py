import sys

S = int(sys.stdin.readline())
n = 1
total = 0
count = 0

while total <= S:
    total += n
    n += 1
    count += 1

print(count - 1)
