N = int(input())
names = set(tuple(input().split()) for _ in range(N))

if len(names) != N:
    print('Yes')
else:
    print('No')


