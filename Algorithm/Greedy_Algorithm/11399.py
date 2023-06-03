import sys

n = int(sys.stdin.readline().rstrip())
durations = list(map(int, sys.stdin.readline().rstrip().split()))

durations = sorted(durations)

total = 0
waiting = 0

for i in range(n):
    waiting += durations[i]
    total += waiting

print(total)
