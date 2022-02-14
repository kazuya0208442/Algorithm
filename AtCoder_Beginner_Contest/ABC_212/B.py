

X = list(map(int, list(input())))

if len(set(X)) == 1:
    print('Weak')
    exit()

for i in range(3):
    if (X[i] + 1) % 10 != X[i+1]:
        print('Strong')
        break

else:
    print('Weak')

