import sys

lines = []
for l in sys.stdin:
    lines.append(l.rstrip('\r\n'))

s = list(lines[0])
stack = []
ans = ''

for v in s:
    if len(stack) == 0 or stack[-1][0] != v:
        stack.append([v, 1])
    else:
        stack[-1][1] += 1

for string, count in stack:
    ans += string + str(count)

print(ans)
# print(stack)








