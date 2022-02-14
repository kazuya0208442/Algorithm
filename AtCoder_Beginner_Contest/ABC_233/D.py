N, K = map(int, input().split())
A = list(map(int, input().split()))       # 8 -3 5 7 0 -4
S = [0]

for i in range(N):
    S.append(S[i]+A[i])         # [a0,    a1,     a2,        a3,         a4,     ]
                                # [0,     a0,    a0+a1,   a0+a1+a2,   a0+a1+a2+a3]
                                # [S0,    S1,     S2,        S3,         S4      ]
                                # 2項目から４項目までの和 => indexにすると現実の数字にー１すればいいので、a1 ~ a3 までの和 => S4(Sは添え字のa4を持ってないので、１大きい数を選ぶ) - S1(Sは添え字のa1を持ってないので、同じ数を選ぶ)
                                # Sn の添え字nを見たら、a0 ~ an-1 までの和だよ。一個少ない数までの和しか持ってない。

# Sr - Sl = K -> Sl = Sr - K  Srを決めたらSlが決まる。SLが存在するかをチェック。
# Sr - Sl = K のように部分和を求めるときはSnは一回求めてしまえば、そのままそのSnを使える。

dict = {0: 1}
ans = 0

for i in range(1, len(S)):
    Sr = S[i]
    Sl = Sr - K

    if Sl in dict:
        ans += dict[Sl]
    
    dict[Sr] = dict.get(Sr, 0) + 1

print(ans)

