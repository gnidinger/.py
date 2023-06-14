import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
A = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
m, k = map(int, sys.stdin.readline().rstrip().split())
B = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(m)]

result = ''

for i in range(n):
    for j in range(k):
        sum = 0
        for l in range(m):
            sum += A[i][l] * B[l][j]
        result += str(sum) + ' '
    result += '\n'

print(result)
