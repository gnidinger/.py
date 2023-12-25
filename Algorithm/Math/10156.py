import sys

K, N, M = map(int, input().split())
answer = max(0, K * N - M)
print(answer)
