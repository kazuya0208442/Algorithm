# 町をめぐる順番はN!通りある。
# それぞれのルートでの総距離を求めて、ルートの総数で割ればいい
# len(distance) で割ればよかった。N!の関数作らなくてもよかった。

import itertools

N = int(input())
x_position = [0]
y_position = [0]
distance = []

for _ in range(N):
    x, y = map(int, input().split())
    x_position.append(x)
    y_position.append(y)

for route in itertools.permutations(range(1, N+1)):
    dist = 0
    for i in range(N-1):
        diff_x = x_position[route[i]] - x_position[route[i+1]]
        diff_y = y_position[route[i]] - y_position[route[i+1]]
        dist += (diff_x**2 + diff_y**2)**(1/2)
    distance.append(dist)

def count_roop(N: int) -> int:
    ans = 1
    while N:
        ans *= N
        N -= 1
    return ans

print(sum(distance)/count_roop(N))











