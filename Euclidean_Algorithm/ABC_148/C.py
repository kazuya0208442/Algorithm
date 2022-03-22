import sys
from typing import List

def main(lines: List):
    A, B = map(int, lines[0].split())

    def greatest_common_divisor(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a
    
    print(A*B // greatest_common_divisor(A, B))

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)