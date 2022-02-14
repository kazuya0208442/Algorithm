S = list(input())
option = len(S) - 1
ans = 0

for bit in range(1 << (option)):
    plus_position = S[:]           # [:]をつけないと、Sも書き換わってしまうから気を付けて。
    for i in range(option):
        if (bit >> i) & 1:
            plus_position[i] = plus_position[i] + '+'
    
    temp = list(map(int, ''.join(plus_position).split('+')))
    # print(temp)
    for j in temp:
        ans += j
    # print(ans)

print(ans)










