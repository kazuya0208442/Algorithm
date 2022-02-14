

# H, W, N = map(int, input().split())
# AB = [list(map(int, input().split())) for _ in range(N)]
# AB.sort()
# temp = AB[0][0]
# AB[0][0] = 1

# # print(AB)

# for i in range(1, N):
#     if AB[i][0] != temp:
#         temp = AB[i][0]
#         AB[i][0] = AB[i-1][0] + 1
#     else:
#         AB[i][0] = AB[i-1][0]

# # print(AB)

# AB.sort(key = lambda x: x[1])

# # print(AB)

# temp = AB[0][1]
# AB[0][1] = 1

# # print(AB)

# for i in range(1, N):
#     if AB[i][1] != temp:
#         temp = AB[i][0]
#         AB[i][1] = AB[i-1][1] + 1
#     else:
#         AB[i][1] = AB[i-1][1]
    

# # print(AB)

# for li in AB:
#     print(*li)








H, W, N = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
A = []
B = []


for ab in AB:
    A.append(ab[0])
    B.append(ab[1])

print(A)
print(B)

A = sorted(set(A), key=A.index)
B = sorted(set(B), key=B.index)










