import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == 0:
        break
    elif a == b == c:
        print('Equilateral')
    elif a + b <= c or a + c <= b or b + c <= a:
        print('Invalid')
    elif a == b or a == c or b == c:
        print('Isosceles')
    elif a != b and b != c:
        print('Scalene')
