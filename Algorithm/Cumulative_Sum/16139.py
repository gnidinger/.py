import sys

string = sys.stdin.readline().rstrip()
n = len(string)
q = int(sys.stdin.readline().rstrip())
lst = [[0] * (n + 1) for _ in range(26)]

for i, char in enumerate(string):
    for j in range(26):
        lst[j][i + 1] = lst[j][i]
    lst[ord(char) - ord('a')][i + 1] += 1

for _ in range(q):
    query = list(sys.stdin.readline().rstrip().split())
    char = ord(query[0]) - ord('a')
    start = int(query[1])
    end = int(query[2])

    count = lst[char][end + 1] - lst[char][start]

    print(count)
