import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
mod = 1000000007

fac = [0] * (n + 1)
fac[0] = fac[1] = 1

for i in range(2, n + 1):
    fac[i] = (fac[i - 1] * i) % mod

denominator = (fac[k] * fac[n - k]) % mod


def power(base, exponent):
    if exponent == 1:
        return base % mod

    half = power(base, exponent // 2)

    if exponent % 2 == 0:
        return (half**2) % mod
    else:
        return (((half**2) % mod) * base) % mod


print((fac[n] * power(denominator, mod - 2)) % mod)
