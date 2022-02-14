# [1,2,3] -> [1,2,4,3]  両サイドに何を持っているのかのリストを作った。
# 更新作業が4つあることに注意せよ。


N = int(input())
S = list(input())

right = [-1] * (N+1)
left = [-1] * (N+1)

for i in range(len(S)):
    if S[i] == 'R':
        if right[i] == -1:
            right[i] = i+1
            left[i+1] = i
        else:
            temp = right[i]
            right[i] = i+1
            right[i+1] = temp
            left[i+1] = i
            left[temp] = i+1

    elif S[i] == 'L':
        if left[i] == -1:
            left[i] = i+1
            right[i+1] = i
        else:
            temp = left[i]
            left[i] = i+1
            left[i+1] = temp
            right[i+1] = i
            right[temp] = i+1

# print(right)
# print(left)

index = left.index(-1)

while index != -1:
    print(index, end=' ')
    index = right[index]




# 逆順で解く方法でもやってみて





