

A, B, C, X = map(int, input().split())

if X <= A:
    print(1)
elif A+1 <= X <= B:
    print(C / (B - (A+1) + 1))
else:
    print(0)




