import sys
from typing import List, Optional

def main(lines: List):
    N = int(lines[0])
    on_and_off = list(map(int, lines[1].split()))
    cumulative_sum = [0]
    right = 6
    ans = 0

    for i in range(N):
        if on_and_off[i] == 1:
            cumulative_sum.append(cumulative_sum[i] + 0)
        else:
            cumulative_sum.append(cumulative_sum[i] + 1)

    for left in range(N-6):
        if (right+1 < N+1) and (cumulative_sum[right+1] - cumulative_sum[left] < 2):
            right += 1
            continue

        while (right+1 < N+1) and (cumulative_sum[right+1] - cumulative_sum[right-6] >= 2):
            right += 1
        
        ans = max(ans, right - left)
    
    print(ans)







if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)


