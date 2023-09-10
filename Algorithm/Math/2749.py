import sys


def matrix_multiply(a, b, mod):
    return [
        [
            (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % mod,
            (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % mod,
        ],
        [
            (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % mod,
            (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % mod,
        ],
    ]


def matrix_pow(matrix, exp, mod):
    if exp == 1:
        return matrix
    if exp % 2 == 0:
        half_pow = matrix_pow(matrix, exp // 2, mod)
        return matrix_multiply(half_pow, half_pow, mod)
    else:
        return matrix_multiply(matrix, matrix_pow(matrix, exp - 1, mod), mod)


n = int(sys.stdin.readline().rstrip())
mod = 1000000
pisano_period = 1500000
n = n % pisano_period

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    result_matrix = matrix_pow([[1, 1], [1, 0]], n - 1, mod)
    print(result_matrix[0][0])
