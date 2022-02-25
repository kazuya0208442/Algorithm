N, Q = map(int, input().split())
S = list(input())
cumulative_sum = [0, 0]

for i in range(N-1):
    if S[i] + S[i+1] == 'AC':
        cumulative_sum.append(cumulative_sum[i+1] + 1)
    else:
        cumulative_sum.append(cumulative_sum[i+1])

for _ in range(Q):
    l, r = map(int, input().split())
    print(cumulative_sum[r] - cumulative_sum[l])