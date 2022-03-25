import sys
from typing import List, Optional
from collections import defaultdict

def main(lines: List):
    N = int(lines[0])

    if N % 2 == 1:
        exit()
    
    for bit in range(1<<N):
        cumulative_sum = 0
        ans = ''
        for i in reversed(range(N)):
            if (bit >> i) & 1:
                cumulative_sum -= 1
                ans += ')'
            else:
                cumulative_sum += 1
                ans += '('
            if cumulative_sum < 0:
                break
        else:
            if cumulative_sum == 0:
                print(ans)





if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)


