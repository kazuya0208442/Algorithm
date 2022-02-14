# S = list(map(ord, list(input())))
# T = list(map(ord, list(input())))
# dif = []

# # print(S)
# # print(T)

# for i in range(len(S)):
#     dif.append(S[i] - T[i])

# # print(dif)

# set_dif = set(dif)
# list_dif = list(set_dif)

# if len(set_dif) == 1:
#     print('Yes')
# elif len(set_dif) == 2 and abs(list_dif[0]) + abs(list_dif[1]) == 26:
#     print('Yes')
# else:
#     print('No')






# import string して、alphabet = string.ascii_lowercase, alphabet = string.ascii_uppercase
# TLEになちゃった！！！

# import string

# # print(string.ascii_lowercase)     # abcdefghijklmnopqrstuvwxyz
# # print(string.ascii_uppercase)     # ABCDEFGHIJKLMNOPQRSTUVWXYZ

# S = input()
# T = input()
# alphabet = string.ascii_lowercase

# for shift in range(len(alphabet)):
#     ans = ''
#     for s in S:
#         index = (alphabet.index(s) + shift) % len(alphabet)
#         ans += alphabet[index]                        # 多分文字列の作成で、計算量が大きくなっている。これを避けよう。
    
#     if ans == T:
#         print('Yes')
#         exit()

# print('No')





# string と setを使って解いてみる。非負整数 K であることを忘れずに。

# import string

# S = input()
# T = input()
# diff_set = set()

# alphabet = string.ascii_lowercase

# for i in range(len(S)):
#     diff = (alphabet.index(T[i]) - alphabet.index(S[i])+26) % len(alphabet)
#     diff_set.add(diff)

# # print(diff_set)
    
# if len(diff_set) == 1:
#     print('Yes')
# else:
#     print('No')


#  zab         ->  25, 0, 1
#  abc         ->   0, 1, 2
# diff         -> -25, 1, 1
# diff+26      ->   1, 27, 27
# (diff+26)%26 ->   1, 1, 1






# zip を使う

S = input()
T = input()

diff_set = {(ord(a)-ord(b)+26)%26 for a, b in zip(S, T)}

# print(diff_set)
# print(chr(97))

if len(diff_set) == 1:
    print('Yes')
else:
    print('No')







    



# 優秀な回答１

# def solve():
#     s = input()
#     t = input()
#     u = set((ord(a)- ord(b)) % 26 for a,b in zip(s,t))
#     return "Yes" if len(u) == 1 else "No"
 
# print(solve())