# 区間がちょうど被った時はout
# 区間の右端でsort
# 区間の右端よりも大きいかどうかで判別
# 区間を1つずつforで見ていって、r < startなら、その区間を採用

N = int(input())
interval = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[1])
r = -float('inf')
ans = 0

for start, goal in interval:
    if r < start:
        ans += 1
        r = goal

print(ans)









