import sys
import math


def is_prime(a):
    cnt = 0
    for i in range(1, int(a**0.5) + 1):
        if a % i == 0:
            cnt += 1
    if cnt == 1:
        return True


t = int(sys.stdin.readline())


for i in range(t):
    n = int(sys.stdin.readline())
    a = b = n // 2
    while a > 0:
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1
