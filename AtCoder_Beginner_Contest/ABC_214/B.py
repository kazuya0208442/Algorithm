# a <= b <= c とする。 
# 3a <= S : a <= S/3     3a <= T : a <= T**(1/3)
# a+2b <= S : b <= (S-a)/2       b**2 <= T/a : b <= (T/a)**(1/2)
# c <= S-(a+b)         c <= T/(a*b)
# 最悪ケースでも10**6でいける、計算すると。条件が、かつ、だから、小さいほうに合わせないと、片方の条件を破ることになる。


# S, T = map(int, input().split())
# ans = 0

# amax = min(S//3, T**(1/3))
# bmax = min(S//2, T**(1/2))
# cmax = min(S, T)

# for a in range(amax+1):
#     for b in range(bmax+1):
#         for c in range(cmax+1):
#             if a+b+c <= S and a*b*c <= T:
#                 ans += 1

# print(ans)

# 敗因　まずa <= b <= c　これを満たしてない、勝手に俺がつけたやつだから。




# a,b,cが最悪どこまでで行くのかは、二つの条件のうち小さいほうの値まで。最悪ケースでも10**6でいける

S, T = map(int, input().split())
ans = 0

for a in range(S+1):
    for b in range(S+1):
        for c in range(S+1):
            if a+b+c <= S and a*b*c <= T:
                ans += 1


print(ans)



