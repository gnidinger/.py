import sys
from itertools import combinations

l, c = map(int, sys.stdin.readline().rstrip().split())
letters = sys.stdin.readline().rstrip().split()
letters.sort()

tmp = set("aeiou")

for password in combinations(letters, l):
    if len(set(password) & tmp) >= 1 and len(set(password) - tmp) >= 2:
        print("".join(password))
