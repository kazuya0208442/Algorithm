import sys
from typing import List

def main(lines: List):
    A, B, C, D = map(int, lines[0].split())

    if A < C:
        print('Takahashi')
    elif A > C:
        print('Aoki')
    elif B < D:
        print('Takahashi')
    elif B > D:
        print('Aoki')
    else:
        print('Takahashi')


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)