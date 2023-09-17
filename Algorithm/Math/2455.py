import sys

current = 0
mx = 0

for _ in range(4):
    off, on = map(int, sys.stdin.readline().rstrip().split())
    current = current - off + on
    if current > mx:
        mx = current

print(mx)
