
def main():
    N, P, Q = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    # print(A)

    # for i in range(N):      # 先に割っておこうと思ったけど遅くなるかも
    #     A[i] %= P

    # print(A)


    for i in range(N-4):
        for j in range(i+1, N-3):
            for k in range(j+1, N-2):
                for x in range(k+1, N-1):
                    for y in range(x+1, N):
                        # if A[i] * A[j] * A[k] * A[x] * A[y] % P == Q:    # 2つの整数の積をある正の整数で割った時の余りの関係。abをmで割った余りは、rr'をmで割った余りに等しい。
                        # if (A[i] % P) * A[j] % P * A[k] % P * A[x] % P * A[y] % P == Q:   # 積がでかくなる前に余りを先に計算しておく,これでもだめだTLEだわ
                        # if A[i] * A[j] * A[k] * A[x] * A[y] % P == Q:     # 先にPで割っといたから、これでも行けるかと思ったけどだめだな、小分けにしよう。
                        if (((((A[i] * A[j]) % P) * A[k] % P) * A[x] % P) * A[y] % P) == Q: # 1つ掛け算するごとに剰余を求めて、大きくならないようにする。
                            count += 1
    return print(count)

main()           # コードべた書きの方が５倍も速いのはなんでだろう。。。。。。。。。関数にすると遅くなるのかな。。。

