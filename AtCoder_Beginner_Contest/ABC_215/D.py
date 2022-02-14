

def gcd(x, y):
    if x == 0 or y==0:
        return 0
    while y:
        x, y = y, x%y
    return x

N, M = map(int, input().split())
A = list(map(int, input().split()))
ans = []

for k in range(1, M+1):
    for i in range(N):
        if i == N-1 and gcd(A[i], k) == 1:
            ans.append(k)
        if gcd(A[i], k) == 1:
            continue
        else:
            break
    

print(len(ans))

for v in ans:
    print(v)