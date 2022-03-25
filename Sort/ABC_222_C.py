# Optional[X] は Union[X, None] と同値です。
# None のようなシングルトンと比較をする場合は、常に is か is not を使うべきです。絶対に等値演算子を使わないでください。

import sys
from typing import List, Optional
from collections import defaultdict

def main(lines: List):
    N, M = map(int, lines[0].split())
    patterns = [list(pattern) for pattern in lines[1:]]
    rank = [[0, v] for v in range(1, 2*N + 1)]

    def judge(x: str, y: str, index_x: int, index_y: int) -> Optional[int]:
        if x == y:
            return
        elif (x == 'G') and (y == 'C'):
            return index_x
        elif (x == 'C') and (y == 'P'):
            return index_x
        elif (x == 'P') and (y == 'G'):
            return index_x
        else:
            return index_y
    
    for i in range(M):
        for j in range(0, 2*N, 2):
            x_win_count, x_number = rank[j]
            y_win_count, y_number = rank[j+1]
            x_pattern = patterns[x_number-1][i]
            y_pattern = patterns[y_number-1][i]

            judgement = judge(x_pattern, y_pattern, j, j+1)

            if judgement is not None:
                rank[judgement][0] += 1
        rank.sort(key=lambda x: (-x[0], x[1]))
    
    for win_count, number in rank:
        print(number)



if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)


