import sys

n, b = map(int, sys.stdin.readline().rstrip().split())
p = 1000
A = [[int(x) % 1000 for x in sys.stdin.readline().rstrip().split()] for _ in range(n)]


def multiply(A, B):
    global n
    C = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += (A[i][k] * B[k][j]) % p
            C[i][j] %= p
    return C


def pow(A, exponent):
    if exponent == 1:
        return A

    temp = pow(A, exponent // 2)
    temp = multiply(temp, temp)

    if exponent % 2 == 1:
        temp = multiply(temp, A)

    return temp


result = pow(A, b)

for i in result:
    print(' '.join(map(str, i)))
