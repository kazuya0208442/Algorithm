

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    for i_small in range(1, H):
        for i_large in range(i_small+1, H+1):
            for j_small in range(1, W):
                for j_large in range(j_small+1, W+1):
                    if A[i_small-1][j_small-1] + A[i_large-1][j_large-1] > A[i_large-1][j_small-1] + A[i_small-1][j_large-1]:
                        return print('No')
    
    return print('Yes')

main()