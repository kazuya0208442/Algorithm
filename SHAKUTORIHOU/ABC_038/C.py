N = int(input())
numbers = list(map(int, input().split()))
r = 0
ans = 0

for l in range(N):
    while r+1 < N and numbers[r] < numbers[r+1]:
        r += 1
    ans += r - l + 1
    if r == l:
        r += 1
print(ans)
    








