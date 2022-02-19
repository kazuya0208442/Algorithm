

x1, y1, x2, y2 = map(int, input().split())
group_1 = set()
group_2 = set()

for X, Y in [[2,1], [1,2]]:
    group_1.add((x1+X, y1+Y))
    group_2.add((x2+X, y2+Y))

    group_1.add((x1-X, y1+Y))
    group_2.add((x2-X, y2+Y))

    group_1.add((x1+X, y1-Y))
    group_2.add((x2+X, y2-Y))

    group_1.add((x1-X ,y1-Y))
    group_2.add((x2-X ,y2-Y))

if group_1 & group_2:
    print('Yes')
else:
    print('No')







