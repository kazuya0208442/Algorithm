import sys
from typing import List

def main(lines: List):
    N, M = map(int, lines[0].split())
    A = list(map(int, lines[1].split()))
    C = list(map(int, lines[2].split()))
    B_0 = C[0] // A[0]
    B_N = C[N] // A[N]
    


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)