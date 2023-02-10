import sys


def backjoon(a):
    count = 0

    if a < 100:
        return a
    else:
        for i in range(100, a + 1):
            if i // 100 - (i // 10) % 10 == (i // 10) % 10 - i % 10:
                count += 1

    return count + 99


x = int(sys.stdin.readline())

print(backjoon(x))
