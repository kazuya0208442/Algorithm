
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A_and_B = list(set(A) & set(B))
condition_1 = 0
condition_2 = 0

for v in A_and_B:
    if A.index(v) == B.index(v):
        condition_1 += 1
    else:
        condition_2 += 1

print(condition_1)
print(condition_2)




