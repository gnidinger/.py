import sys

result = []

for i in range(9):
    a = list(map(int, sys.stdin.readline().split()))
    result += a

x = max(result)
y = result.index(x)

i = y // 9 + 1
j = y % 9 + 1

print(x)
print(i, j)
