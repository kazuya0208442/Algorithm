# def main():
#     H, W = map(int, input().split())
#     A = [list(map(int, input().split())) for _ in range(H)]

#     for i_small in range(1, H):
#         for i_large in range(i_small+1, H+1):
#             for j_small in range(1, W):
#                 for j_large in range(j_small+1, W+1):
#                     if A[i_small-1][j_small-1] + A[i_large-1][j_large-1] > A[i_large-1][j_small-1] + A[i_small-1][j_large-1]:
#                         return print('No')
    
#     return print('Yes')

# main()





H, W = map(int, input().split())
matrix = [0] + [[0] + list(map(int, input().split())) for _ in range(H)]

for i1 in range(1, H):
    for i2 in range(i1+1, H+1):
        for j1 in range(1, W):
            for j2 in range(j1+1, W+1):
                if matrix[i1][j1] + matrix[i2][j2] > matrix[i2][j1] + matrix[i1][j2]:
                    print('No')
                    exit()

print('Yes')


