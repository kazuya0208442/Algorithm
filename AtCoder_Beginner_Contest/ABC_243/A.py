

V, *ml_list = map(int, input().split())


for i in range(10**8):
    if V - ml_list[i%3] >= 0:
        V -= ml_list[i%3]
    else:
        if i%3 == 0:
            print('F')
        elif i%3 == 1:
            print('M')
        else:
            print('T')
        exit()









