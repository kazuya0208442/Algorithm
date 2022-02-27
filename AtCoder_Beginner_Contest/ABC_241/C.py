from typing import List
N = int(input())
grid = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if grid[i][j] == '.':
            grid[i][j] = 0
        else:
            grid[i][j] = 1

def check_6_left_to_right(grid):
    for row in grid:
        cumulataive_sum = [0]
        for i in range(len(row)):
            cumulataive_sum.append(cumulataive_sum[i] + row[i])
        for j in range(len(cumulataive_sum) - 6):                # Snのnに6個の差がないといけない。S6 - S0 みたいな。で、最後は、S(n+1) - S(n+1 - 6) になるので、jはn-5まで回せばいい。
            if cumulataive_sum[j+6] - cumulataive_sum[j] >= 4:
                print('Yes')
                exit()


left_up_to_right_bottom = []

for i in range(N):
    for j in range(N):
        if i == 0:
            left_up_to_right_bottom.append([grid[i][j]])
            continue

        if j == 0:
            left_up_to_right_bottom.append([grid[i][j]])
        elif j < i:
            left_up_to_right_bottom[-j-1].append(grid[i][j])  # j=0 の時に最新の奴が作られているから、それのさらにもう一個前を表すために-1しているよ。
        else:
            left_up_to_right_bottom[j-i].append(grid[i][j])

right_up_to_left_bottom = []

for i in range(N):
    grid[i].reverse()
    for j in range(N):
        if i == 0:
            right_up_to_left_bottom.append([grid[i][j]])
            continue

        if j == 0:
            right_up_to_left_bottom.append([grid[i][j]])
        elif j < i:
            right_up_to_left_bottom[-j-1].append(grid[i][j])
        else:
            right_up_to_left_bottom[j-i].append(grid[i][j])

# print(left_up_to_right_bottom)
# print(len(left_up_to_right_bottom))

# 1 2 3
# 4 5 6
# 7 8 9   # これの左上から右下は求めた。

# 3 2 1
# 6 5 4
# 9 8 7   # 上の行列の行を反転させた。これの左上から右下を求めれば、元の行列の右上から左下を求めたことになる。

check_6_left_to_right(grid)
check_6_left_to_right(list(zip(*grid)))
check_6_left_to_right(left_up_to_right_bottom)
check_6_left_to_right(right_up_to_left_bottom)

print('No')







