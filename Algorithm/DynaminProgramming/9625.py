import sys

K = int(sys.stdin.readline().rstrip())

count_A = 1
count_B = 0

for _ in range(K):
    new_count_A = count_B
    new_count_B = count_A + count_B

    count_A = new_count_A
    count_B = new_count_B

print(count_A, count_B)
