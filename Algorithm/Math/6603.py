import sys
from itertools import combinations

while True:
    input_data = list(map(int, sys.stdin.readline().rstrip().split()))
    if input_data[0] == 0:
        break
    del input_data[0]
    for comb in combinations(input_data, 6):
        print(" ".join(map(str, comb)))
    print()
