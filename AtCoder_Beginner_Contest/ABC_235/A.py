# abc = list(map(int, list(input())))
# # print(*abc[1:2])

# bca = abc[1]*100 + abc[2]*10 + abc[0]
# cab = abc[2]*100 + abc[0]*10 + abc[1]
# abc = abc[0]*100 + abc[1]*10 + abc[2]

# print(abc+bca+cab)






# abc = int(input())

# a = abc // 100
# b = abc // 10 % 10
# c = abc % 10

# bca = 100*b + 10*c + a 
# cab = 100*c + 10*a + b 

# print(abc+bca+cab)


# 文字もiteratorだから、展開できる。

a, b, c = input()
abc = a + b + c
bca = b + c + a
cab = c + a + b
ans = int(abc) + int(bca) + int(cab)
print(ans)