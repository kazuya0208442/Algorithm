# [number, count] の形で、筒の中に積み重ねていく。
# number = count になったら、このリストは消える。
# 圧縮操作みたいなもの
# stack: スタックとは、最も基本的なデータ構造の一つで、要素が入ってきた順に一列に並べ、後に入れた要素から順に取り出すという規則で出し入れを行うもの。

N = int(input())
ball_number = list(map(int, input().split()))
stack = []
ball_count = 0

for i in range(N):
    if (len(stack) == 0) or (stack[-1][0] != ball_number[i]):
        stack.append([ball_number[i], 1])
        ball_count += 1
        print(ball_count)
    elif stack[-1][0] == ball_number[i]:
        stack[-1][1] += 1
        ball_count += 1
        if stack[-1][0] == stack[-1][1]:
            ball_count -= stack[-1][1]
            stack.pop()
            print(ball_count)
        else:
            print(ball_count)



        












