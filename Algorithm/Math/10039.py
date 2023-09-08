import sys

input = sys.stdin.readline
result = 0

for _ in range(5):
    a = int(input())
    if a < 40:
        result += 40
    else:
        result += a

print(result // 5)
