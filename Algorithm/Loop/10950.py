a = int(input())

b = []

for _ in range(a):
    x, y = map(int, input().split())
    b.append(x + y)

for i in range(1, a + 1):
    print(b[i - 1])