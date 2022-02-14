# 累積和つかう
# S(7) - S(4) = a4 + a5 + a6 -> [4, 7) までの和
# S(1) - S(0) = a0 - 0  -> [0, 1)

# S(7) : a0 + a1 + a2 + a3 + a4 + a5 + a6
# S(4) : a0 + a1 + a2 + a3

# S = list(input())
# K = int(input())
# accumulation = [0]
# ans = 0

# for i in range(len(S)):
#     if S[i] == 'X':
#         accumulation.append(accumulation[i] + 0)
#     elif S[i] == '.':
#         accumulation.append(accumulation[i] + 1)



# for i in range(len(S)):
#     l = i
#     r = len(S)

#     if accumulation[r] - accumulation[l] <= K:  # [l, r)の累積和 -> l項目から最後までの累積和のこと
#         ans = max(ans, (r-1) - l + 1)
#         continue

#     while r-l > 1:    # [i, r) のrを求めている。
#         mid = (l+r) // 2
#         if accumulation[mid] - accumulation[i] > K:   # [i, mid) の和を求めている
#             r = mid
#         elif accumulation[mid] - accumulation[i] <= K:
#             l = mid
#     ans = max(ans, (l-1) - i + 1)

# print(ans)



            




# 尺取り法で攻めるぜ

S = [0 if v == 'X' else 1 for v in input()]     # list内包表記のif else の使い方
K = int(input())
r = 0
sum = 0
ans = 0

for i in range(len(S)):
    # while r+1 < len(S) and sum+S[r+1] <= K:     # [l,r] 両方含むパターン。おすすめしない。
    #     sum += S[r+1]
    #     r += 1
    # ans = max(ans, r-l+1)

    while r < len(S) and sum+S[r] <= K:     # S[r] を足して、Kを超えたらout。つまり、r番目まではいけない。その一個前まで。[l,r)の半開区間で持つといいらしい。
        sum += S[r]
        r += 1
    ans = max(ans, r-i)
    sum -= S[i]

print(ans)