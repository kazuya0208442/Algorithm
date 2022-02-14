# S, T, X = map(int, input().split())
# time = [0]*24

# if S < T:
#     for i in range(S, T+1):
#         time[i] = 1
# else:
#     for i in range(S, 24):
#         time[i] = 1
#     for j in range(T+1):
#         time[j] = 1

# if time[X] == 1 and T != X:
#     print('Yes')
# else:
#     print('No')

# print(time)




# 24時 = 0時 なので、[0,1,2,3...23] のように24で割った余りの世界になる。
# フラグを立てていく作戦

S, T, X = map(int, input().split())
is_lighted = [False] * (24)

if S < T:
    for time in range(S, T+1):
        is_lighted[time] = True
    if X == T:
        print('No')
    elif is_lighted[X]:
        print('Yes')
    else:
        print('No')

else:
    for time in range(S, 24):
        is_lighted[time] = True
    for time in range(T+1):
        is_lighted[time] = True
    if X == T:
        print('No')
    elif is_lighted[X]:
        print('Yes')
    else:
        print('No')









