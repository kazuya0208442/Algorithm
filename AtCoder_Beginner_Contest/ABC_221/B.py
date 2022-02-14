

S = list(input())
T = list(input())
n = len(S)
swap = False

if S == T:
    swap = True
else:
    for i in range(n-1):
        S[i], S[i+1] = S[i+1], S[i]
        if S == T:
            swap = True
            break
        S[i], S[i+1] = S[i+1], S[i]

if swap:
    print('Yes')
else:
    print('No')