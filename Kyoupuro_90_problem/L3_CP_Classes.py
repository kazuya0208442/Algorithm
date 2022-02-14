# from collections import defaultdict

# def main():
#     N = int(input())
#     A_list = list(map(int, input().split()))
#     Q = int(input())
#     B_list = [int(input()) for _ in range(Q)]
#     min_dict = defaultdict(lambda: float('inf'))              # デフォルトで辞書に最大値を入れといて、比較していく作戦はTLEだったのでやめよう。

#     for i in range(N):
#         for j in range(Q):
#             dif = abs(A_list[i] - B_list[j])
#             if min_dict[j] > dif:
#                 min_dict[j] = dif

#     # print(min_dict)

#     for i in range(Q):
#         print(min_dict[i])

# main()


# from collections import defaultdict

# def main():
#     N = int(input())
#     A_list = list(map(int, input().split()))
#     Q = int(input())
#     B_list = [int(input()) for _ in range(Q)]
#     min_dict = defaultdict(list)                   # dict_items([(0, [688, 1088, 1688, 112]), (1, [1008, 1408, 2008, 208]), (2, [229, 171, 771, 1029])])みたいになるよ

#     for i in range(N):
#         for j in range(Q):
#             dif = abs(A_list[i] - B_list[j])
#             min_dict[j].append(dif)

#     for k in range(Q):
#         print(min(min_dict[k]))
    
#     # print(min_dict.items())

# main()                                 # だめだTLEだわ。importすると遅いのかな。list in listでやってみるか。



def main():
    N = int(input())
    A_list = list(map(int, input().split()))
    Q = int(input())
    B_list = [int(input()) for _ in range(Q)]
    min_list = [[] for _ in range(Q)]                   

    for i in range(N):
        for j in range(Q):
            dif = abs(A_list[i] - B_list[j])
            min_list[j].append(dif)

    for k in range(Q):
        print(min(min_list[k]))
    

main()          # list in listでもだめだ。全探索の限界だ。これは二分探索の出番だ。。。。



