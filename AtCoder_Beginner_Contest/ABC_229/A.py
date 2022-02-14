# S1 = input()
# S2 = input()

# if S1[0] == '.' and S2[0] == '#' and S1[1] == '#' and S2[1] == '.':
#     print('No')
# elif S1[0] == '#' and S2[0] == '.' and S1[1] == '.' and S2[1] == '#':
#     print('No')
# else:
#     print('Yes')




# #が合計で 2 つ以上含まれる。
# ３つ以上だと必ず行き来できる。
# 1つは、条件違反
# 2つで、行き来できないパターンは、斜め配置の時。

S1 = input()
S2 = input()

if S1[0] == '#' and S1[1] == '.' and S2[0] == '.' and S2[1] == '#':
    print('No')
elif S1[0] == '.' and S1[1] == '#' and S2[0] == '#' and S2[1] == '.':
    print('No')
else:
    print('Yes')
