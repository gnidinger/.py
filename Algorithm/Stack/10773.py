import sys

k = int(sys.stdin.readline().rstrip())

result = list()

for _ in range(k):
    a = int(sys.stdin.readline().rstrip())
    if a == 0:
        del result[-1]
    else:
        result.append(a)

print(sum(result))
