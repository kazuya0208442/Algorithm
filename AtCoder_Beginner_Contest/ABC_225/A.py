# import itertools

# def main():
#     S = list(input())
#     A = list(itertools.permutations(S))
#     # print(A)
#     print(len(set(A)))

# main()           # 反則技みたいなやつ笑 3文字固定であることにきづかん

# S = set(input())  # {'d', 'r', 'a', 'f', 's'}

# if len(S) == 3: print('6')
# elif len(S) == 2: print('3')
# else: print('1') 







# 3文字の並び替え 3!通りある。
# 重複がある場合は、その個数をNとして、N!で割ればいい

# category_num = len(set(input()))

# if category_num == 3:
#     print(6)
# elif category_num == 2:
#     print(3)
# else:
#     print(1)





# 順列を生成する

import itertools
category_num = set()

for p in itertools.permutations(input()):
    category_num.add(p)

print(len(category_num))




