a, b = map(int, input().split())
c = int(input())

time = a + (b + c) // 60
minute = (b + c) % 60

print(time % 24, minute)