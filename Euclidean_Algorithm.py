# ユークリッドの互除法

# 3355 / 2379 = 1 ... 976
# 2379 / 976 = 2 ... 427
# 976 / 427 = 2 ... 122
# 427 / 122 = 3 ... 61
# 122 / 61 = 2
# 最大公約数は「６１」。余りで割る数を割る。余りが０の時の割る数が最大公約数。

# a / b = 商 ... a%b 
# b / a%b = 商 ... b%(a%b) 
#   a    b           a%b
# a%b / b%(a%b) = 商 ... (a%b)%(b%(a%b))
#    a       b               a       b

# aの位置を「割られる数」、bの位置を「割る数」とすると、次の計算に行くには
# 初めのbを、aの位置の「割られる数」にセットして、余りa%bを「割る数」の位置にセットする。

# 計算に必要なのは、(割る数, 2数の除算の余り)なので、
# a = b 
# b = a%b

#3 ユークリッドの互除法による最大公約数を求める関数  a<bの時は初めのループでa,bが入れ替わる。
def gcd_e(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd_e(48,36))
print(gcd_e(36, 48))


