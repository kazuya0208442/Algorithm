# xor は二回やると元の値に戻る。　A xor C xor A = C = B xor A

A, B = map(int, input().split())

bi = A ^ B
print(bi)


