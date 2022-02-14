
def two_check():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    all_two_ok = True

    while all_two_ok:
        all_two_ok = False
        for index, value in enumerate(A):
            if value % 2 == 0:
                A[index] = value // 2
            else:
                return (A, count)
        count += 1
        all_two_ok = True
    return (A, count)

print(two_check())
