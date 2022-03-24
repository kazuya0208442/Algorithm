# できるだけ少ないパンチで多くの壁を破壊したい。
# 壁が重ならないように配置した時の、壁の枚数が答え
# 区間の右側が小さいほうから、破壊していけばいい

import sys
from typing import List

def main(lines: List):
    N, D = map(int, lines[0].split())
    left_and_right = sorted([list(map(int, L_R.split())) for L_R in lines[1:]], key=lambda x: x[1])
    inf = float('inf')
    pointer = -inf
    count_wall = 0

    for left, right in left_and_right:
        if pointer + D - 1 < left:
            count_wall += 1
            pointer = right
    
    print(count_wall)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)


