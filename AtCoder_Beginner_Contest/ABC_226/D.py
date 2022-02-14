# N = int(input())
# xy = [list(map(int, input().split())) for _ in range(N)]
# magics = set()

# def gcd(x, y):
#     while y:
#         x, y = y, x % y
#     return x

# # print(gcd(-6, -30))

# for i in range(N-1):
#     for j in range(i+1, N):
#         difx = xy[i][0] - xy[j][0]
#         dify = xy[i][1] - xy[j][1]
#         gcd_num = abs(gcd(difx, dify))

#         magic_a = (difx//gcd_num, dify//gcd_num)
#         magic_b = (-difx//gcd_num, -dify//gcd_num)

#         magics.add(magic_a)
#         magics.add(magic_b)

# # print(magics)
# print(len(magics))





# できるだけ覚える魔法は少なくしたい。
# 大きく移動する魔法よりも、移動回数は増えるけど、小さく移動する魔法の方が、いろんな場所に行ける。
# 2点の座標の差を、最大公約数で割って、最小単位にするイメージ。
# 使った魔法をsetで管理して、重複を防ぐ。

# 最大公約数 gcd (greatest common divisor) 必ず、余りが０になるときがくる。
# 最小公倍数 lcm (least common multiple)
# 最小公倍数の求め方 lcm(a, b) = a * b / gcd(a, b)

# gcd(-11, -79) = -1 のように、2数が持っている約数で-1があるなら、それも含まれる。
# |gcd|をとれば、単位長さが正の数で得られる。

# 片方の経路だけ入れてしまって、答えが1/2になってた。これはまずい。
# {[1,1] [-1,-1]} の時にこれを2倍すると、４つになるけど、2点しかない場合、答えは２つである。

# 19と0の最大公約数は19ですか？０ですか？または違う数か、公約数はなしですか？
# 公約数は共通した約数です。
# どの数だろうが0をかけてしまえば0になるので、
# すべての整数は0の約数と言えます。
# ならば、19の約数すべてが公約数です。
# よって、最大公約数は19となります。

N = int(input())
positions = [list(map(int, input().split())) for _ in range(N)]
unique_magic = set()

def gcd(a: int, b: int) -> int:
    # print(a,b)
    while b:
        a, b = b, a%b
        # print(a,b)
    return a
# print(gcd(0, -79))


for i in range(N):
    for j in range(i+1, N):
        x1, y1 = positions[i]
        x2, y2 = positions[j]
        x_diff = x2 - x1
        y_diff = y2 - y1
        gcd_num = abs(gcd(x_diff, y_diff))
        magic = tuple([x_diff//gcd_num, y_diff//gcd_num])
        magic_reverse = tuple([-x_diff//gcd_num, -y_diff//gcd_num])

        if magic not in unique_magic:
            unique_magic.add(magic)
        if magic_reverse not in unique_magic:
            unique_magic.add(magic_reverse)


print(len(unique_magic))









