import sys

n = int(sys.stdin.readline().strip())
sum_of_plugs = 0

for _ in range(n):
    sum_of_plugs += int(sys.stdin.readline().strip())

print(sum_of_plugs - n + 1)
