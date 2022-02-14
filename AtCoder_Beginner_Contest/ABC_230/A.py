# N = int(input())

# if N >= 42:
#     N += 1

# N = str(N)
# N = '000' + N
# # N = list(N)
# N = N[-3:]

# print('AGC' + N)




N = int(input())

if N >= 42:
    N += 1

ans = 'AGC' + ''.join(list('00' + str(N))[-3:])
print(ans)