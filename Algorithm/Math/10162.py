import sys

T = int(sys.stdin.readline().rstrip())

A, B, C = 0, 0, 0


if T % 10 != 0:
    print(-1)
else:
    A = T // 300
    T %= 300

    B = T // 60
    T %= 60

    C = T // 10

    print(f"{A} {B} {C}")
