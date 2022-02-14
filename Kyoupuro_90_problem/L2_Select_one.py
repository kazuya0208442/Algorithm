

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    dif = 0

    for i in range(N):
        dif += abs(A[i] - B[i])

    if K < dif or K % 2 != dif % 2:
        print('No')
    else:
        print('Yes')
    
main()
