a, b, c = map(int, input().split())

list = [a, b, c]

if a == b == c:
    print(10000 + a * 1000)
elif a == b and b != c:
    print(1000 + a * 100)
elif a != b and b == c:
    print(1000 + b * 100)
elif a == c and b != c:
    print(1000 + a * 100)
else:
    print(max(list) * 100)