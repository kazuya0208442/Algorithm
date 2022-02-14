

N = int(input())
A = list(map(int, input().split()))
degree = [False] * (360)
degree[0] = True
sum_degree = 0

for num in A:
    if sum_degree + num < 360:
        sum_degree += num
        degree[sum_degree] = True
    else:
        sum_degree = (sum_degree + num) % 360
        degree[sum_degree] = True

l = 0
r = 0
ans = 0

for i in range(1, 360):
    if degree[i]:
        r = i
        ans = max(ans, r-l)
        l = r

ans = max(ans, 360-l)

print(ans)



