import sys

n, k = map(int, sys.stdin.readline().split())

factorial_n = 1
for i in range(2, n):
    factorial_n *= i

factorial_k = 1
for i in range(2, k):
    factorial_k *= i

factorial_n_k = 1
for i in range(2, n - k + 1):
    factorial_n_k *= i

result = factorial_n // (factorial_k * factorial_n_k)

print(result)
