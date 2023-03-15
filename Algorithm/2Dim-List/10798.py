import sys

a = []

for i in range(5):
    a += list(sys.stdin.readline().split())

result = ''

for i in range(15):
    for j in range(5):
        if len(a[j]) > i:
            result += a[j][i]

print(result)
