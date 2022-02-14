# 332332
# N, K, A = map(int, input().split())

# index = A-1
# to = index + K - 1
# ans_index = to % N

# print(ans_index + 1)





# nums  [1,2,3,4,5]
# index [0,1,2,3,4]
# 3の人から４枚渡す。-> 1の人が最後
# indexが(3-1)の人に、(K-1)を足すと５になって、%5すろと０になる
# つまり、nums[((A-1) + (K-1)) % N] が答え。indexに戻して、自分に配る分を引いた枚数分進む

N, K, A = map(int, input().split())
print((((A-1) + (K-1)) % N)+1)


