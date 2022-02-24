# 1 <= N <= 10**9 この範囲の中で、買うことができる整数で、最大の数字は、２分探索で求められる。
# A * N + B * d(N) <= X であれば、N を購入可能

A, B, X = map(int, input().split())
left = -1                 # N = 0 は必ず買える。範囲外だし大丈夫でしょ。
right = 10**9 + 1         # 範囲外の整数であれば買うことは不可能

while right - left > 1:
    mid = (left + right) // 2
    digit = int(len(str(mid)))
    if (A*mid + B*digit <= X):
        left = mid
    else:
        right = mid

if left == -1:
    print(0)
else:
    print(left)