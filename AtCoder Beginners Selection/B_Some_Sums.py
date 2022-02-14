# def main():
#     values = list(map(int, input().split()))

#     for i in range(values[0]):
#         divmod(i+1, 10)            失敗。listにして取り出さなくても、普通に=で置いていい。

# N, A, B = map(int, input().split())
# # print(N ,A, B)
# print(sum(i for i in range(1, N+1) if A <= sum(map(int, str(i))) <= B))

def main():
    N, A, B = map(int, input().split())
    # print(N)
    ans_list = []

    for i in range(N+1):
        if A <= sum(map(int, str(i))) <= B:
            ans_list.append(i)
    
    return print(sum(ans_list))

main()












