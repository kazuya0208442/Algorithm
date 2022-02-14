# 先にN人の0 or 1を決めておく。後は、1の証言だけが正しいので、１の証言と、あらかじめ決めた0or1が一致しているかを見る。


N = int(input())
testimony = []
ans = 0

for _ in range(N):
    A = int(input())
    temp = [list(map(int, input().split())) for _ in range(A)]
    testimony.append(temp)


# print(testimony)

for i in range(1 << N):
    true_false_list = []
    for j in range(N):
        if (i >> j) & 1:
            true_false_list.append(1)
        else:
            true_false_list.append(0)
    out = False
    for k in range(N):
        if true_false_list[k] == 1:
            for person_num, bit in testimony[k]:
                if true_false_list[person_num-1] != bit:
                    out = True
                    break
            if out:
                break
    else:
        ans = max(ans, sum(true_false_list))


print(ans)






