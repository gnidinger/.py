a = int(input())

b = (a % 10) * 10 + (a // 10 + a % 10) % 10
cycle = 1

while b != a:
    cycle += 1
    b = (b % 10) * 10 + (b // 10 + b % 10) % 10
    
print(cycle)