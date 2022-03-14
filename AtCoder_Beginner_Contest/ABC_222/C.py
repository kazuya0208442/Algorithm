# N, M = map(int, input().split())
# patterns = [input() for _ in range(2*N)]
# people = 2 * N
# rank = [[i, 0] for i in range(people)]

# def win(a, b):
#     if a == 'G' and b == 'C':
#         return True
#     if a == 'C' and b == 'P':
#         return True
#     if a == 'P' and b == 'G':
#         return True
#     return False

# for i in range(M):
#     for j in range(0, people, 2):
#         a = patterns[rank[j][0]][i]
#         b = patterns[rank[j+1][0]][i]
#         if win(a, b):
#             rank[j][1] -= 1
#         if win(b, a):
#             rank[j+1][1] -= 1

#     rank = sorted(rank, key=lambda x: (x[1], x[0]))

# for index, score in rank:
#     print(index+1)






    



import sys

lines = []
for l in sys.stdin:
    lines.append(l.rstrip('\r\n'))

N, M = map(int, lines[0].split())
patterns = [[list(pattern), 0, index] for index, pattern in enumerate(lines[1:])]
win_count = [[] for _ in range(M+1)]
win_count[0] = patterns

def judge(x, y, index_x, index_y):
    if x == y:
        return
    if x == 'G' and y == 'C':
        return index_x
    elif x == 'C' and y == 'P':
        return index_x
    elif x == 'P' and y == 'G':
        return index_x
    else:
        return index_y

for game_count in range(M):
    for v in win_count:
        for i in range(0, len(v) ,2):
            win_index = judge(v[i][0][game_count], v[i+1][0][game_count], i, i+1)
            if win_index:
                v[win_index][1] += 1
                v.remove(v[win_index])
                
        
    for j in range(M, -1, -1):
        if len(win_count[j]) == 0:
            continue
        else:
            win_count[j].sort(key=lambda x: x[2])




