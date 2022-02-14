# N = int(input())
# H = list(map(int, input().split()))
# ans = H[0]

# for i in range(N-1):
#     if H[i] < H[i+1]:
#         ans = H[i+1]
#     else:
#         print(ans)
#         exit()

# print(ans)






# whileで攻める

N = int(input())
H = list(map(int, input().split()))
position = 0

# while position < N-1 and  H[position] < H[position+1]:
while H[position] < H[position+1]:
    position += 1

print(H[position])