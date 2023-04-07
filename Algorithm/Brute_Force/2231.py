import sys

n = int(sys.stdin.readline())

for i in range(n + 1):
    if i == n:
        print(0)

    x = (
        i // 1000000
        + (i % 1000000) // 100000
        + (i % 100000) // 10000
        + (i % 10000) // 1000
        + (i % 1000) // 100
        + (i % 100) // 10
        + i % 10
        + i
    )

    if x == n:
        print(i)
        break
