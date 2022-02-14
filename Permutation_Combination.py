# 順列 選んで並べるやつ
def nPr(n, r):
   result = 1
   for i in range(r):
       result *= (n - i)
   return result


# 組み合わせ 
def nCr(n,r):
   if (r == 0) or (r == n):
       return 1
   
   return nCr(n - 1, r - 1) + nCr(n - 1, r)


print(nPr(5, 2))
print(nCr(5, 2))