# from collections import defaultdict

# N = int(input())
# A = list(map(int, input().split()))
# d = defaultdict(int)

# for i in range(len(A)):
#     d[A[i]] += 1

# list_of_key = list(d.keys())
# list_of_value = list(d.values())

# index = list_of_value.index(3)

# print(list_of_key[index])





# getの第二引数を使ってみるぜ、defaultdict使わなくてもいける。listの場合も同じように第二引数に空のlistを渡せばいい。

# N = int(input())
# A = input().split()
# dict = {}

# for v in A:
#     dict[v] = dict.get(v, 0) + 1

# for k, v in dict.items():
#     if v == 3:
#         print(k)
#         break





# ビットごとの排他的論理和を表す記号を ⊕ とします。

# a⊕a=0 であることを用います。 入力で与えられた A 全ての排他的論理和を考えると、
# 上述の性質より 4 枚存在するようなカードについての排他的論理和は 0 となり、3 枚しか存在しないカードの値が残ります。

# すなわち、答えは A 
# 1
# ​
#  ⊕A 
# 2
# ​
#  ⊕…A 
# 4N−1
# ​
#   と一致します。


N = int(input())
A = list(map(int, input().split()))
ans = A[0]

for i in range(1, 4*N-1):
    ans = ans ^ A[i]

print(ans)
