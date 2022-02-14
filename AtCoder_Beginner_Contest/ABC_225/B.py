

# def main():
#     N = int(input())
#     a_b_list = [list(map(int, input().split())) for _ in range(N-1)]
#     A = [[] for _ in range(N)]

#     for i in range(N-1):
#         a_b = a_b_list[i]
#         A[a_b[0]-1].append(a_b[1])
#         A[a_b[1]-1].append(a_b[0])

#     for j in range(N):
#         if len(A[j]) == N-1:
#             return print('Yes')
    
#     print('No')
# main()               # もう少しシンプルに書こうか


N = int(input())            # 各頂点がいくつの点とつながっているのかの個数を求める方針
N_list = [0] * (N + 1)

for _ in range(N-1):
    a, b = map(int, input().split())
    N_list[a] += 1
    N_list[b] += 1

if max(N_list) == N-1:
    print('Yes')
else:
    print('No')



