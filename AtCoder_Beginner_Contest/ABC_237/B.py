# H, W = map(int, input().split())
# A = [list(map(int, input().split())) for _ in range(H)]

# T_A = list(zip(*A))
# print(A)
# print(T_A)

# for row in T_A:
#     print(*row)




# A(i,j) = B(j,i) という定義通りに実装してみる

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [[0]*H for _ in range(W)]

for i in range(H):
    for j in range(W):
        B[j][i] = A[i][j]

for b in B:
    print(*b)
