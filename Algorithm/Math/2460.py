import sys

max_people = 0
current_people = 0

for _ in range(10):
    out, in_ = map(int, sys.stdin.readline().split())
    current_people += in_ - out
    max_people = max(max_people, current_people)

print(max_people)
