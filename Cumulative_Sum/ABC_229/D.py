# 二分探索の全部Yesの場合はありうるし省くこともできる
# 二分探索の全部Noの場合はありえないのでは？
# ある区間の累積和を求めるためには、２つの要素が必要。
# 左端がNoになることはあり得るのか？問題
# K = 0 が最小である。
# 左端は 0 or 1 のどちらか。

# 0 項目から x 項目 までの和 -> S(x+1) - S(0)
# 0 項目から 4 項目 までの和 -> S(5) - S(0) = 3

# 左端がNoになるパターン
# K = 0
# 0 項目から 0 項目 までの和 -> S(1) - S(0) = 1 > K

# 左端がforループで動いていくから、その都度、左端を調べて、S(1) - S(0) = 1 > K になってたら、そこからスタートしても0なので、0を返してcontinueだな。

import sys
from typing import List

def main(lines: List):
    S = list(lines[0])
    K = int(lines[1])
    cumulative_sum = [0]
    ans = 0

    for i in range(len(S)):
        if S[i] == 'X':
            cumulative_sum.append(cumulative_sum[i] + 0)
        else:
            cumulative_sum.append(cumulative_sum[i] + 1)
    
    for j in range(len(S)):
        left = j
        right = len(cumulative_sum) - 1

        if cumulative_sum[-1] - cumulative_sum[left] <= K:   # 全部 Yes の場合を省く
            ans = max(ans, len(S) - left)
            continue

        elif cumulative_sum[left+1] - cumulative_sum[left] > K:
            continue

        while right - left > 1:
            mid = (left + right) // 2
            if cumulative_sum[mid] - cumulative_sum[j] <= K:
                left = mid
            else:
                right = mid
        
        ans = max(ans, left - j)
        
        # leftの条件 -> S(left) - S(j) <= K -> [j, left)
        # j項目からleft-1項目までの累積和がK以下ってこと。
        
    print(ans)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)





