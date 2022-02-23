s = list(input())
stack = []
ans = ''

for i in range(len(s)):
    if (len(stack) == 0) or stack[-1].get(s[i]) == None:
        stack.append({s[i]: 1})
    else:
        stack[-1][s[i]] += 1

for dict in stack:
    for key, value in dict.items():
        ans += (key + str(value))

print(ans)