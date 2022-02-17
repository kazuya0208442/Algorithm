# N 以下の約数の列挙をする。
# 約数ならば、N % i = 0 になる。必ず割り切れる。

# i <= N**(1/2) の範囲を調べればオッケー
# while i * i <= N と書き換えることが可能

# 6 * 6 = 36 のように、約数が重複する場合に、２回カウントしないようにすべき。

from typing import List

from matplotlib.pyplot import show

def show_divisor(N: int) -> List[int]:
    lower_divisor, upper_divisor = [], []
    i = 1

    while i * i <= N:
        if N % i == 0:
            lower_divisor.append(i)
            if i != N // i:
                upper_divisor.append(N//i)
        i += 1
    
    return lower_divisor + upper_divisor[::-1]

print(show_divisor(105))

























# def make_divisors(n):
#     lower_divisors , upper_divisors = [], []
#     i = 1
#     while i*i <= n:
#         if n % i == 0:
#             lower_divisors.append(i)
#             if i != n // i:
#                 upper_divisors.append(n//i)
#         i += 1
#     return lower_divisors + upper_divisors[::-1]