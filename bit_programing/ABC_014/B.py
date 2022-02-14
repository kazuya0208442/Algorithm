n, X = map(int, input().split())
products = list(map(int, input().split()))
sum = 0

for i in range(n):
    print(bin(X >> i))
    print((X >> i) & 1)
    if (X >> i) & 1:
        sum += products[i]

print(sum)








