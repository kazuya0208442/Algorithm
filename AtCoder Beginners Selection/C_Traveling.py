
def main():
    N = int(input())
    grids = [list(map(int, input().split())) for _ in range(N)]

    t = 0
    x = 0
    y = 0

    for i in range(N):
        t = grids[i][0] - t
        x = grids[i][1] - x
        y = grids[i][2] - y

        if t < abs(x) + abs(y) or (abs(x) + abs(y)) % 2 != t % 2:
            return print('No')
    print('Yes')

main()