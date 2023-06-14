import sys

n = int(sys.stdin.readline().rstrip())
p = 1000000007

if n == 1:
    print(1)
    exit()

matrix = [[1, 1], [1, 0]]


def multiply(a, b):
    global p

    x = len(a)
    y = len(b[0])
    z = len(b)

    result = [[0 for _ in range(y)] for _ in range(x)]

    for i in range(x):
        for j in range(y):
            for k in range(z):
                result[i][j] += (a[i][k] * b[k][j]) % p
                result[i][j] %= p

    return result


def power(matrix, exp):
    if exp == 1:
        return matrix

    temp = power(matrix, exp // 2)
    result = multiply(temp, temp)

    if exp % 2 == 1:
        result = multiply(result, matrix)

    return result


result = power(matrix, n - 1)

print(result[0][0])
