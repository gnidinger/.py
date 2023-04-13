import sys
import math


def eratos(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return [x for x in range(n + 1) if is_prime[x]]


while True:
    a = int(sys.stdin.readline().rstrip())
    if a == 0:
        break
    b = 2 * a
    print(len(eratos(b)) - len(eratos(a)))
