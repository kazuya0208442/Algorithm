# Nから逆算する。

N = int(input())
ans = ''

while N:
    if N % 2 == 0:
        N //= 2
        ans += 'B'
    else:
        N -= 1
        ans += 'A'

new_ans = ''.join(list(reversed(ans)))
print(new_ans)



