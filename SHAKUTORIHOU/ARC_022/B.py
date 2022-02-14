N = int(input())
taste = list(map(int, input().split()))
r = 1
ans = 0
seen = {taste[0]}

for l in range(N):
    if not seen:
        seen.add(taste[l])
    while (r < N) and (not taste[r] in seen):
        seen.add(taste[r])
        r += 1
    ans = max(ans, r-l)
    if r-l == 1:
        r += 1
    seen.discard(taste[l])

print(ans)








