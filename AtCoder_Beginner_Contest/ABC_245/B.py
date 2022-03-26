import sys
from typing import List

def main(lines: List):
    N = int(lines[0])
    numbers = set(map(int, lines[1].split()))

    for v in range(2001):
        if v not in numbers:
            print(v)
            exit()



if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)