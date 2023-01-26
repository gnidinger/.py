a = int(input())
b = int(input())

x = b // 100
y = (b // 10) % 10
z = b % 10

print(a * z, a * y, a * x, a * b, sep='\n')