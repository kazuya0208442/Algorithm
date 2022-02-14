

A = input()


if int(A[-1]) <= 2:
    print(A[:-2] + '-')
elif int(A[-1]) <= 6:
    print(A[:-2])
else:
    print(A[:-2] + '+')




