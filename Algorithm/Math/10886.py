import sys

n = int(input())
cute = 0

for _ in range(n):
    vote = int(input())
    cute += vote

if cute > n // 2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
