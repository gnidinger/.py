import sys

a, b, c = map(int, sys.stdin.readline().rstrip().split())


def pow(a, exponent, mod):
    if exponent == 1:
        return a % mod

    temp = pow(a, exponent // 2, mod)

    if exponent % 2 == 0:
        return (temp**2) % mod
    else:
        return (((temp**2) % mod) * a) % mod


print(pow(a, b, c))
