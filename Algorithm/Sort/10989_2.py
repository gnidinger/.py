import sys

n = int(sys.stdin.readline())
counting = [0] * 10001
result = [] * n

for _ in range(n):
    counting[int(sys.stdin.readline())] += 1

for i in range(10001):
    if counting[i] != 0:
        for j in range(counting[i]):
            print(i)
