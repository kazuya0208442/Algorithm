# 0 を一つも含まない集合の数
# 9 を一つも含まない集合の数
# 0 and 9 を一つも含まない集合の数
# 0 or 9 を一つも含まない集合の数 <-> 0 and 9 を両方含む集合の数
# 全通りの数


N = int(input())
mod = 10**9 + 7



# 整理するために式を書いた。
# zero_excluded = 9**N
# nine_excluded = 9**N
# zero_and_nine_excluded = 8**N
# zero_or_nine_excluded = zero_excluded + nine_excluded - zero_and_nine_excluded

# zero_and_nine_included = 10**N - zero_or_nine_excluded
# print(zero_and_nine_included)





# 指数の計算を関数にした。
def count(x: int, exponential: int):
    ans = 1
    for _ in range(exponential):
        ans *= x
        ans %= mod

    return ans


zero_excluded = count(9, N)
nine_excluded = count(9, N)
zero_and_nine_excluded = count(8, N)
zero_or_nine_excluded = (zero_excluded + nine_excluded - zero_and_nine_excluded) % mod

zero_and_nine_included = (count(10, N) - zero_or_nine_excluded) % mod
print(zero_and_nine_included)