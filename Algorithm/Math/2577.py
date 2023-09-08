import sys

a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
c = int(sys.stdin.readline().rstrip())

result = a * b * c
count = [0] * 10

while result > 0:
    count[result % 10] += 1
    result //= 10

for x in count:
    print(x)
