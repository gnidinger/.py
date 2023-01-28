a = int(input())
b = int(input())
c = 0

for i in range(b):
    x, y = map(int, input().split())
    c += x * y

if a == c:
    print('Yes')

print('No')