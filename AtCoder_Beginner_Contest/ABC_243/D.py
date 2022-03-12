import sys

lines = []
for l in sys.stdin:
    lines.append(l.rstrip('\r\n'))

N, X = map(int, lines[0].split())
S = list(lines[1])

for v in S:
    if v == 'U':
        X //= 2
    elif v == 'R':
        X = 2 * X + 1
    else:
        X *= 2

print(X)
