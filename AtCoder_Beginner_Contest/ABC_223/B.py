# S=input()
 
# X=[S]
# N=len(S)
# for i in range(N-1):
#     S=S[1:]+S[0]
#     X.append(S)
 
# X.sort()
 
# print(X[0])
# print(X[-1])      #模範解答だよ


# def main():
#     S = input()
#     S_list = [S,]

#     for i in range(len(S)-1):
#         S = S[1:] + S[0]
#         S_list.append(S)
    
#     ans_list = sorted(S_list)
#     # print(S_list)
#     # print(ans_list)
#     print(ans_list[0])
#     print(ans_list[-1])

# main()

S = input()
A = []

for i in range(len(S)):
    A.append(S)
    S = S[1:] + S[0]

A_sort = sorted(A)

print(min(A_sort))
print(max(A_sort))



