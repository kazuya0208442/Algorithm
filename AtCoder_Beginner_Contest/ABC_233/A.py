# X, Y = map(int, input().split())
# dif = Y-X

# if X >= Y:
#     print(0)
# elif dif % 10 == 0:
#     print(dif//10)
# else:
#     print(dif//10 + 1)




# 小数点以下の切り上げで行ける

X, Y = map(int, input().split())

if X >= Y:
    print(0)
else:
    print(-(-(Y-X)//10))
    