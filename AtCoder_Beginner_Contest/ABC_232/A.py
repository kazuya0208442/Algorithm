# S = list(input())

# a = int(S[0])
# b = int(S[2])

# print(a*b)




# 文字はiteratorなので、そのまま取り出せるよ。

# fir_int, cross, sec_int = input()
# fir_int = int(fir_int)
# sec_int = int(sec_int)

# print(fir_int*sec_int)



# split()の応用

fir_int, sec_int = map(int, input().split('x'))
print(fir_int*sec_int)