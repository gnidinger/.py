import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
p = 1000000007

fac = [0] * (n + 1)
fac[0] = fac[1] = 1

for i in range(2, n + 1):
    fac[i] = (fac[i - 1] * i) % p

denominator = (fac[k] * fac[n - k]) % p


def power(base, exponent):
    if exponent == 1:
        return base % p

    half = power(base, exponent // 2)

    if exponent % 2 == 0:
        return (half**2) % p
    else:
        return (((half**2) % p) * base) % p


print((fac[n] * power(denominator, p - 2)) % p)
