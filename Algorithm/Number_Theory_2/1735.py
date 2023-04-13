import sys
import math

a, x = map(int, sys.stdin.readline().split())
b, y = map(int, sys.stdin.readline().split())

z = math.lcm(x, y)

a = a * z // x
b = b * z // y

c = math.gcd(a + b, z)

print((a + b) // c, z // c)
