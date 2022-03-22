# https://qiita.com/drken/items/0c88a37eec520f82b788#2-1-%E5%8D%98%E7%B4%94%E3%81%AA%E6%9C%80%E5%A4%A7%E5%85%AC%E7%B4%84%E6%95%B0%E3%82%B2%E3%83%BC
# 線分上の格子点の数の個数

import sys
from typing import List

def main(lines: List):
    ax, ay = map(int, lines[0].split())
    bx, by = map(int, lines[1].split())

    diff_x = abs(ax - bx)
    diff_y = abs(ay - by)

    def greatest_common_divisor(a: int, b:int) -> int:
        while b:
            a, b = b, a % b
        return a
    
    gcd = greatest_common_divisor(diff_x, diff_y)

    print(gcd - 1)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)