import sys
from typing import List

def main(lines: List):
    N, K = map(int, lines[0].split())
    A = list(map(int, lines[1].split()))
    B = list(map(int, lines[2].split()))
    A_and_B = list(zip(A, B))
    DP = [[False, False] for _ in range(N)]
    DP[0] = [True, True]

    # print(A_and_B)

    for i in range(1, N):
        for j in range(2):
            if (DP[i-1][0]) and (abs(A_and_B[i-1][0] - A_and_B[i][j]) <= K):
                DP[i][j] = True
            if (DP[i-1][1]) and (abs(A_and_B[i-1][1] - A_and_B[i][j]) <= K):
                DP[i][j] = True
    
    # print(DP)
    if True in DP[N-1]:
        print('Yes')
    else:
        print('No')




if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)