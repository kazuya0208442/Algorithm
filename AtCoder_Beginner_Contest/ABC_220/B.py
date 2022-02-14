

K = int(input())
A, B = input().split()

def k_to_10(x, k):
    res = 0
    for i in range(len(x)):
        res = res * k + int(x[i])
    return res

print(k_to_10(A, K) * k_to_10(B, K))
