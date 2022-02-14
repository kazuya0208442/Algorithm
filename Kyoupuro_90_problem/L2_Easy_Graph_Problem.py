from collections import defaultdict

def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)]
    ans_dic = defaultdict(list)     # {1: [2, 3], 2: [1, 3, 5, 4], 3: [1, 2], 5: [2], 4: [2]}) こんな感じ。
    less_count = defaultdict(int)   # defaultdict(<class 'int'>, {2: 1, 3: 2, 4: 1, 5: 1}) 各頂点ごとに条件を満たす点の数を辞書にした。

    for i in range(M):
        a_b = A[i]
        ans_dic[a_b[0]].append(a_b[1])
        ans_dic[a_b[1]].append(a_b[0])
    
    for j in range(N):
        point_list = ans_dic[j+1]
        for k in range(len(point_list)):
            if j+1 > point_list[k]:
                less_count[j+1] += 1            #問題は1スタートなのでj+1でずらす。

    ans = list(less_count.values()).count(1)

    # print(ans_dic)
    # print(less_count)
    # print(list(less_count.values()))
    print(ans)

main()