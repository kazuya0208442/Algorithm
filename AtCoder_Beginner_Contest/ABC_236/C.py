

N, M = map(int, input().split())
S = input().split()
T = set(input().split())

for i in range(N):
    if S[i] in T:
        print('Yes')
    else:
        print('No')