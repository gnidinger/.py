import sys
import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


while True:
    a = int(sys.stdin.readline())
    if a == 0:
        break
    b = 2 * a
    cnt = 0
    for i in range(a + 1, b + 1):
        if is_prime(i):
            cnt += 1
    print(cnt)
