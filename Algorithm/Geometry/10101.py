import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

if a + b + c == 180:
    if a == b == c:
        print('Equilateral')
    elif a == b or a == c or b == c:
        print('Isosceles')
    elif a != b and b != c:
        print('Scalene')
else:
    print('Error')
