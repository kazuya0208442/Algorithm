import sys
from typing import List
sys.setrecursionlimit(10**6)

def main(lines: List):
    N, X = map(int, lines[0].split())
    ball_numbers = []
    global ans
    ans = 0

    for s in lines[1:]:
        L, *numbers = map(int, s.split())
        ball_numbers.append(numbers)
    
    def dfs(index: int, product: int):

        if (index == N-1) and (product == X):
            global ans
            ans += 1
            return
        elif index == N-1:
            return

        for v in ball_numbers[index+1]:
            if product * v > X:
                continue
            dfs(index+1, product*v)
    
    for v in ball_numbers[0]:
        dfs(0, v)
    
    print(ans)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)