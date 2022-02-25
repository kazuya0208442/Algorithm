def cumulative_sum_max() -> int:
    n, k = map(int, input().split())

    if (n == 0) and (k == 0):
        for ans in ans_list:
            print(ans)
        exit()

    numbers = []
    cumulative_sum = [0]
    ans = 0

    for _ in range(n):
        numbers.append(int(input()))

    for i in range(n):
        cumulative_sum.append(cumulative_sum[i] + numbers[i])

    for j in range(n-k+1):
        ans = max(ans, cumulative_sum[j+k] - cumulative_sum[j])

    ans_list.append(ans)

ans_list = []

while True:
    cumulative_sum_max()
    
