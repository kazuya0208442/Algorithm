# X 項目から X 項目までの和は、S(X+1) - S(X)    1個のみの和の時はこうなる
# L 項目から R 項目までの和は、S(R+1) - S(L)

# L 項目から R 項目までの和が K の場合、S(R+1) - S(L) = K
# S(L) = S(R+1) - K
# 0 <= R <= N をforループで回せば、S(L) の値が決まるので。そのS(L)がいくつあるのかを調べる。

import sys
from typing import List
from collections import defaultdict

def main(lines: List):
    N, K = map(int, lines[0].split())
    numbers = list(map(int, lines[1].split()))
    cumulative_sum = [0]
    cumulative_dict = defaultdict(int)
    ans = 0

    for i in range(N):
        cumulative_sum.append(cumulative_sum[i] + numbers[i])

    for right in range(N):
        cumulative_dict[cumulative_sum[right]] += 1
        sum_left = cumulative_sum[right+1] - K
        if sum_left in cumulative_dict:
            ans += cumulative_dict[sum_left]
    
    print(ans)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)


