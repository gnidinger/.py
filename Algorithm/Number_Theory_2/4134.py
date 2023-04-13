import sys
import math

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    if n <= 1:
        print(2)
        continue
    is_prime = False
    while not is_prime:
        is_prime = True
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                is_prime = False
                break
        if not is_prime:
            n += 1
    print(n)
