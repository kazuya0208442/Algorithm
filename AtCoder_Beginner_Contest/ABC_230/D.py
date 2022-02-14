N, D = map(int, input().split())
wall = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[1])
pointer = 0
punch_count = 0

for i in range(len(wall)):
    if pointer < wall[i][0]:
        pointer = wall[i][1] + D - 1
        punch_count += 1

print(punch_count)




