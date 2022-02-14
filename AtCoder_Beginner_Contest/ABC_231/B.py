# from typing import Counter

# N = int(input())
# S = [input() for _ in range(N)]

# scount = Counter(S)

# # print(max(scount.most_common())[0])

# print(scount.most_common()[0][0])





# defaultdict で行くぜ。

from collections import defaultdict

N = int(input())
dict = defaultdict(int)

for _ in range(N):
    dict[input()] += 1

key_list = list(dict.keys())
value_list = list(dict.values())

max_value = max(value_list)
max_value_index = value_list.index(max_value)
ans = key_list[max_value_index]

print(ans)
