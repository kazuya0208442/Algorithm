# from xmlrpc.client import boolean


# S = list(input())

# def check(string: str, left: int, right: int) -> boolean:
#     while left < right:
#         if string[left] == string[right]:
#             left += 1
#             right -= 1
#         else:
#             return 'No'
#     return 'Yes'

# aをつけたして、回文になってらオッケー。len(S)-1 回aを付けられる.
# その考えはあんまりよくないかも。




# 回文判定はreverse
# 右にaがいくつあるのか調べて、その個数分足して、回文判定してみる。
# 右と左のaの個数で、右－左の個数分じゃないとだめよ。既にaが左にあるのに足してしまってたから。

S = list(input())
a_pointer = len(S) - 1
right_a_count = 0
left_a_count = 0

while a_pointer >= 0 and S[a_pointer] == 'a':
    right_a_count += 1
    a_pointer -= 1

a_pointer = 0

while a_pointer <= len(S) - 1 and S[a_pointer] == 'a':
    left_a_count += 1
    a_pointer += 1

a_count =  right_a_count - left_a_count

new_S = ['a'] * a_count + S
# print(new_S)

reversed_new_S = list(reversed(new_S))
# print(reversed_new_S)

if new_S == reversed_new_S:
    print('Yes')
else:
    print('No')