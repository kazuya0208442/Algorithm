# S = 4ab + 3a + 3b = 7a + 3

# N = int(input())
# S = list(map(int, input().split()))
# X = []

# for i in range(1, 1000):
#     for j in range(1, 150):
#         if 4 * i * j + 3 * i + 3 * j <= 1000:
#             X.append(4 * i * j + 3 * i + 3 * j)

# ans = 0

# for k in range(N):
#     if S[k] not in X:
#         ans += 1


# print(ans)

# S(max) = 1000
# a >= 1, b >= 1
# S = 4ab + 3a + 3b
# a = 1 -> S = 7b + 3 = 1000 -> b = 997/7 = 142.4 ~ 143 
# b = 1 -> S = 7a + 3 -> a ~ 143


N = int(input())
S = list(map(int, input().split()))
ans_set = set()
ans = N

for a in range(1, 144):
    for b in range(1, 144):
        ans_set.add(4*a*b + 3*a + 3*b)

for s in S:
    if s in ans_set:
        ans -= 1

print(ans)








