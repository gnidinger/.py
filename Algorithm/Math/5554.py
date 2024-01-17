import sys

times = [int(sys.stdin.readline()) for _ in range(4)]
total_seconds = sum(times)
minutes = total_seconds // 60
seconds = total_seconds % 60

print(minutes)
print(seconds)
