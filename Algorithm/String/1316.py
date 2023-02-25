import sys

n = int(sys.stdin.readline())

for i in range(n):
    str = sys.stdin.readline()
    for j in str:
        if j * str.count(j) not in str:
            n -= 1
            break

print(n)
