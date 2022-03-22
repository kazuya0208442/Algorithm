import sys
from typing import List

def main(lines: List):
    N, X = map(int, lines[0].split())
    position = list(map(int, lines[1].split()))
    diff_position = []
    gcd = 0


    for v in position:
        diff_position.append(abs(X - v))

    if N == 1:
        print(diff_position[0])
        exit()
    
    def greatest_common_divisor(x, y):
        while y:
            x, y = y, x % y
        return x
    

    for i in range(N):
        gcd = greatest_common_divisor(gcd, diff_position[i])
    
    print(gcd)
    







if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)