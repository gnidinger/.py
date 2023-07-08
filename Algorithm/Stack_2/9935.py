import sys

text = list(sys.stdin.readline().rstrip())
explosion = list(sys.stdin.readline().rstrip())
result = [0 for _ in range(len(text))]
idx = 0


def isExplosive(result, explosion, idx):
    if idx < len(explosion) - 1:
        return False

    for i in range(len(explosion)):
        if explosion[i] != result[idx - len(explosion) + 1 + i]:
            return False

    return True


for c in text:
    result[idx] = c

    if isExplosive(result, explosion, idx):
        idx -= len(explosion)

    idx += 1

print("FRULA" if idx == 0 else "".join(result[:idx]))
