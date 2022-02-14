N = int(input())
A = list(map(int, input().split()))
X = int(input())

sum_A = sum(A)
x = X // sum_A

ans = len(A) * x

y = X - sum_A * x

for i in range(len(A)):
    y -= A[i]
    if y >= 0:
        continue
    else:
        print(ans + i + 1)
        break





