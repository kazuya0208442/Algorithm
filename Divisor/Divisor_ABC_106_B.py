# 約数の個数を数える問題。
# Nの約数の性質: Nは約数で割り切れる。
# N以下の数字でNを割れるのか調べればいい。
# 平方数の約数の個数は奇数になるんだってさ。
# 調べるのはpow(N,1/2)の切り捨て、まででいい。十分だ。

# 1*36= 36   (1,36)
# 2*18= 36   (2,18)
# 3*12= 36   (3,12)
# 4*9 = 36   (4,9)

# 6*6 = 36   (6,6)      # 調べるのはここまででいい。約数はこの時点ですべて出尽くした。

# 9*4 = 36   (9,4)
# 12*3= 36   (12,3)
# 18*2= 36   (18,2)
# 36*1= 36   (36,1)


# num**2 = xとするのがポイント　
# math必要ない。切り捨てオッケー。
# ただ、平方数の時の条件は、int()とかで、加工したらダメ。
# num**2 = x のように書けばいいさ。

# import math

# N = int(input())
# ans = 0


# def count_divisor(x: int) -> int:
#     # limit = int(pow(x, 1/2))
#     limit = int(x ** (1/2))
#     ans = 0
#     for num in range(1, limit+1):
#         if num**2 == x and x % num == 0:    # num**2 = xとするのがポイント
#             ans += 1
#         elif x % num == 0:
#             ans += 2
#     return ans

# for i in range(1, N+1, 2):
#     if count_divisor(i) == 8:
#         ans += 1

# print(ans)
# print(count_divisor(2))



import sys

def main(lines):
    N = int(lines[0])
    ans = 0

    def count_divisor(N: int) -> int:
        lower_divisor = []
        upper_divisor = []
        number = 1

        while number ** 2 <= N:
            if number ** 2 == N:
                lower_divisor.append(number)
                break
            if N % number == 0:
                lower_divisor.append(number)
                upper_divisor.append(N // number)
            number += 1
        
        divisor = lower_divisor + upper_divisor[::-1]

        return len(divisor)
    
    for v in range(1, N+1, 2):
        if count_divisor(v) == 8:
            ans += 1
    
    print(ans)


if __name__ == '__main__':
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip('\r\n'))
    main(lines)












