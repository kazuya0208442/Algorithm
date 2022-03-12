from collections import defaultdict

N = int(input())
X_list = []
Y_list = []
position_dict = defaultdict(list)

for _ in range(N):
    X, Y = map(int, input().split())
    X_list.append(X)
    Y_list.append(Y)

S = list(input())

for i in range(N):
    position_dict[Y_list[i]].append([X_list[i], S[i]])

for v in position_dict.keys():
    position_dict[v].sort()
    R_count = 0
    for X, string in position_dict[v]:
        if string == 'R':
            R_count += 1
        elif R_count == 0 and string == 'L':
            continue
        else:
            print('Yes')
            exit()
        
print('No')






