


def main():
    N = int(input())
    class_and_score = [list(map(int, input().split())) for _ in range(N)]
    Q = int(input())
    low_and_high = [list(map(int, input().split())) for _ in range(Q)]

    cla_one_sum = [0]*N
    cla_two_sum = [0]*N

    for i in range(N):
        if class_and_score[i][0] == 1:
            cla_one_sum[i] += cla_one_sum[i-1] + class_and_score[i][1]
            cla_two_sum[i] = cla_two_sum[i-1]                                   # クラスが１のときにクラス２の操作もする。ひとつ前の値をコピーすれば累積和ができる。
        else:
            cla_two_sum[i] += cla_two_sum[i-1] + class_and_score[i][1]
            cla_one_sum[i] = cla_one_sum[i-1]
    
    # print(cla_one_sum)
    # print(cla_two_sum)

    for j in range(Q):
        K = low_and_high[j][0]

        if K == 1:
            ans_one = cla_one_sum[low_and_high[j][1]-1]
            ans_two = cla_two_sum[low_and_high[j][1]-1]
        else:
            ans_one = cla_one_sum[low_and_high[j][1]-1] - cla_one_sum[low_and_high[j][0]-2] 
            ans_two = cla_two_sum[low_and_high[j][1]-1] - cla_two_sum[low_and_high[j][0]-2]

        print(ans_one, ans_two)

main()