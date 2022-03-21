# N, K = map(int, input().split())

# # n進数を10進数にするには、一桁ずつ見ていく
# # n**0, n**1, n**2 を順番に掛けていけばいい
# # 10で切り捨てれば、一桁ずつ見ていける。n進数だろうがなんだろうが。
# def n_to_ten(x: int, n: int) -> int:
#     ans = 0
#     digit = 0
#     while x:
#         last_num = x % 10
#         ans += last_num * (n ** digit)
#         x //= 10
#         digit += 1
#     return ans

# # 10進数をn進数にするには、nで割った余りを逆順でくっつけていく
# # n で切り捨てていく
# def ten_to_n(x: int, n: int) -> int:
#     if x == 0:                         # 0が来たら文字列を返してしまうので、ここで対処する。
#         return '0'
#     ans = ''
#     while x:                 # x < 1 になったらout 10進数を一桁ずつ取るときをイメージすれば行ける。
#         num = str(x % n) 
#         ans = num + ans
#         x //= n 
#     return ans

# for _ in range(K):
#     N = ten_to_n(n_to_ten(N, 8), 9)
#     N = N.replace('8', '5')
#     N = int(N)

# print(N)











# def Base_10_to_n(X, n):
#     X_dumy = X
#     out = ''
#     while X_dumy>0:
#         out = str(X_dumy%n)+out
#         X_dumy = int(X_dumy/n)
#     return out                # ネットに落ちてたN進数変換


# def Base_10_to_n(X, n):
#     ans = ''

#     while X:
#         ans = str(X % n) + ans
#         X //= n

#     return ans

# print(Base_10_to_n(13, 2))   # 改造してみた。


# def Base_n_to_10(X, n):
#     ans = 0
#     X = str(X)

#     for i in range(len(X)):
#         ans += int(X[i]) * n ** (len(X) - 1 - i)
#     return print(ans)

# Base_n_to_10(1101, 2)           # n進数を10進数に直すのもできた。


# def main():
#     N, K = map(int, input().split())

#     def Base_n_to_10(X, n):
#         ans = 0
#         X = str(X)

#         for i in range(len(X)):
#             ans += int(X[i]) * n ** (len(X) - 1 - i)
#         return ans                    # まずは8->10進数にする。

#     def Base_10_to_n(X, n):
#         ans = ''

#         while X:
#             ans = str(X % n) + ans
#             X //= n

#         if ans == '':
#             ans = '0'

#         return ans
    
#     for i in range(K):
#         base_10_num = Base_n_to_10(N, 8)
#         base_9_num = Base_10_to_n(base_10_num, 9)
#         N = int(base_9_num.replace('8', '5'))

#     return print(N)

# main()







# 練習で解いてみる

import sys
from typing import List



def main(lines: List):
    N, K = map(int, lines[0].split())
    def base_n_to_10(n: int, x: int) -> int:
        base_10 = 0
        digit = 0
        while x:
            last_number = x % 10
            base_10 += last_number * (n ** digit)
            digit += 1
            x //= 10
        return base_10
    
    def base_10_to_n(n: int, x: int) -> int:
        base_n = ''

        if x == 0:
            base_n = '0'

        while x:
            last_number = x % n 
            base_n = str(last_number) + base_n
            x //= n
        
        return base_n
    
    for _ in range(K):
        N = base_10_to_n(9, base_n_to_10(8, N))
        N = int(N.replace('8', '5'))
    
    print(N)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)