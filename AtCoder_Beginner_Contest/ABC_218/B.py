

P = list(map(int, input().split()))
abc = list(chr(ord('a') + i) for i in range(26))
ans = ''

for i in range(len(P)):
    ans += abc[P[i]-1]

print(ans)

