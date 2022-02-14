# N = int(input())
# ans = 0

# for i in range(1, N+1):
#     for j in range(i, -(-N//i)+1):
#         if N//(i*j) - j + 1 > 0:
#             ans += N//(i*j) - j + 1

# # print(ans)
# print(ans)

#         # if -(-N//(i*j)) - j + 1 > 0:
#         #     ans += -(-N//(i*j)) - j + 1          # 完敗した


# N = int(input())
# maxA = int(N ** (1/3))
# maxB = int(N ** (1/2))
# ans = 0
# print(maxA, maxB)

# # A*A*A <= A*B*B <= A*B*C <= N 式変形して範囲を狭めると、  A <= N**(1/3), A <= B <= (N/A)**(1/2), B <= C <= N/(A*B)


# for A in range(1, maxA+1):
#     for B in range(A, maxB+1):
#         maxC = N // (A * B)
#         ans += maxC - B + 1

# print(ans)




# n = int(input())
# ans = 0
 
# for i in range(1, n + 1):
#     if i * i * i > n:
#         break
#     for j in range(i, n + 1):
#         if i * j * j > n:
#             break
#         ans += (n // (i * j)) - j + 1
# print(ans)                              # 模範解答、全部回して、やばかったらbreak



# N = int(input())
# ans = 0

# for A in range(1, N+1):
#     if A*A*A > N:
#         break
#     for B in range(A, N+1):
#         if A*B*B > N:
#             break
#         maxC = N // (A*B)
#         ans += maxC - B + 1

# print(ans)



# 不等式を使って、A,B,Cそれぞれの最大範囲を調べる。

# A**3 <= N  -> A <= N ** (1/3) ~ 4700 -> 1 <= A <= 4700(max)
# AB**2 <= N  -> B <= pow(N/A, 1/2) ~ 320000 -> A <= B <= 320000(max)
# C <= N\AB ~ N -> B <= C <= N

# 不等号があるときは、置き換えて文字の数を減らす。
# Bの上限はAを決めるときに行わないといけない。
# 初めからBの上限を決めてしまいwaだった。

N = int(input())
A_max = int(-(-pow(N, 1/3) // 1)) 
# B_max = int(-(-pow(N, 1/2) // 1))
ans = 0

for A in range(1, A_max+1):
    B_max = int(pow(N/A, 1/2))     # Aが分かったら、Bの上限が分かる。
    for B in range(A, B_max+1):
        # if A * B > N:
        #     break
        temp = N//(A*B) - B + 1
        ans += temp

print(ans)







