# スイッチの点灯パターン2**Nを全探索する。点灯パターンを先に決めておく。
# それぞれのパターンで、点灯を１、消灯を０にして、条件の和を求めて、２で割った余りとpiを比較する。
# その条件をすべてクリアした時だけ、for break ... else を使って求める。


N, M = map(int, input().split())
sum_switch = []
switch_num = []

for _ in range(M):
    temp = list(map(int, input().split()))
    sum_switch.append(temp[0])
    switch_num.append(temp[1:])

p = list(map(int, input().split()))
ans = 0

for i in range(1 << N):
    on_off_list = []
    for j in range(N):
        if (i >> j) & 1:
            on_off_list.append(1)
        else:
            on_off_list.append(0)
    
    for k in range(M):
        sum = 0
        for s in switch_num[k]:
            sum += on_off_list[s-1]
        if sum % 2 == p[k]:
            continue
        else:
            break
    
    else:
        ans += 1

print(ans)









