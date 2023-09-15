import sys

T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    a = a % 10

    if a == 0:
        print(10)
        continue

    cycle = []
    temp = a

    while True:
        if temp in cycle:
            break
        cycle.append(temp)
        temp = (temp * a) % 10

    cycle_len = len(cycle)
    answer = cycle[(b % cycle_len) - 1]
    print(answer if answer != 0 else 10)
