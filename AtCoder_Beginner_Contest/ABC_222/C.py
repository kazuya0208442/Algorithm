


N, M = map(int, input().split())
patterns = [input() for _ in range(2*N)]
people = 2 * N
rank = [[i, 0] for i in range(people)]

def win(a, b):
    if a == 'G' and b == 'C':
        return True
    if a == 'C' and b == 'P':
        return True
    if a == 'P' and b == 'G':
        return True
    return False

for i in range(M):
    for j in range(0, people, 2):
        a = patterns[rank[j][0]][i]
        b = patterns[rank[j+1][0]][i]
        if win(a, b):
            rank[j][1] -= 1
        if win(b, a):
            rank[j+1][1] -= 1

    rank = sorted(rank, key=lambda x: (x[1], x[0]))

for index, score in rank:
    print(index+1)






    
