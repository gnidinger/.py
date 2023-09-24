import sys

word = sys.stdin.readline().rstrip()
cnt = [0] * 26

for char in word:
    index = ord(char) - ord("a")
    cnt[index] += 1

print(" ".join(map(str, cnt)))
