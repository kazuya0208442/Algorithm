# min(X,Y) のおかげで、A,Bの両方とも必要な、最低枚数が分かる。
# どっちかが０なら、0をかけることになり、整合性も合う。
# その時は、AもしくはB単体と2*Cの値段を比べればいい。


A, B, C, X, Y = map(int, input().split())
ans = 0


if A+B > 2*C:
    ans += 2*C * (min(X, Y))
else:
    ans += (A+B) * (min(X, Y))

if X > Y:
    A_needed = X - Y
    if A > 2*C:
        ans += 2*C * A_needed
    else:
        ans += A * A_needed
else:
    B_needed = Y - X
    if B > 2*C:
        ans += 2*C * B_needed
    else:
        ans += B * B_needed

print(ans)









