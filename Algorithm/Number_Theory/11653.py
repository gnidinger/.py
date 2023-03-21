import sys
import math


def is_prime(a):
    cnt = 0
    for i in range(1, a):
        if a % i == 0:
            cnt += 1
    if cnt == 1:
        return True


n = int(sys.stdin.readline())

list = []

for i in range(1, n + 1):
    while n % i == 0 and is_prime(i) == True:
        list.append(i)
        n /= i

list.sort()

print(*list, sep='\n')
