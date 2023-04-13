import sys
import math

t = int(sys.stdin.readline())


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


for _ in range(t):
    n = int(sys.stdin.readline())
    while not is_prime(n):
        n += 1
    print(n)
