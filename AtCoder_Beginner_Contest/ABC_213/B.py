

N = int(input())
A = list(map(int, input().split()))

for i, v in enumerate(A):
    A[i] = [v, i]

A.sort(reverse=True)

print(A[1][1]+1)
# print(A)