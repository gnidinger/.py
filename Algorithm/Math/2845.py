import sys

l, p = map(int, input().split())
article = list(map(int, input().split()))

for i in range(5):
    print(article[i] - l * p, end=" ")
