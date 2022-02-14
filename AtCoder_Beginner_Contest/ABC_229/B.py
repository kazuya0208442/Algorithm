# A, B = map(list, input().split())
# length = min(len(A), len(B))
# A.reverse()
# B.reverse()

# for i in range(length):
#         a, b = map(int, [A[i], B[i]])
#         if a+b < 10:
#             continue
#         else:
#             print('Hard')
#             exit()

# else:
#     print('Easy')



# A, B = map(int, input().split())

# while A and B:
#     a = A % 10
#     b = B % 10

#     if a+b > 9:
#         print('Hard')
#         break
    
#     A //= 10
#     B //= 10

# else:
#     print('Easy')





# 末尾の数字から削っていって、どっちかが0になったら終わり。
# それまでに繰り上がりがあれば、終了

A, B = map(int, input().split())

while A and B:
    A_last = A % 10
    B_last = B % 10
    if A_last + B_last > 9:
        print('Hard')
        exit()
    A //= 10
    B //= 10

print('Easy')
