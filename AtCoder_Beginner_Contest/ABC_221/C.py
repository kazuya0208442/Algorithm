

# 1 <= N <= 1000,000,000 = 10**9
# Nには０でない桁が二つあるので Nmax = 999,999,999 = 10**9 - 1
# 最大で2**9(512)通りの２グループに分ける方法がある。
# 全て０と全て１は分離できていないので省きたい。
# [000,000,000], [000,000,001], [000,000,010], ... [111,111,110], [111,111,111], [1,000,000,000]
# (1 << 1) = 10(2)   (1 << 2) = 100(2**2)   (1 << 3) = 1000(2**3)
# 

N = list(input())
n = len(N)
ans = 0


for bit in range(1, (1 << n) - 1):
    a, b = [], []
    for i in range(n):
        if ((bit >> i) & 1):
            a.append(N[i])
        else:
            b.append(N[i])
    a.sort(reverse=True)
    b.sort(reverse=True)

    x = int(''.join(a))
    y = int(''.join(b))

    ans = max(ans, x*y)

print(ans)


    

    


