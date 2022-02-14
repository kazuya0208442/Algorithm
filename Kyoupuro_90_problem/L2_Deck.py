

# Q = int(input())
# t_x_list = [list(map(int, input().split())) for _ in range(Q)]
# cards = []

# for i in range(Q):
#     t_x = t_x_list[i]

#     if t_x[0] == 1:
#         cards.insert(0, t_x[1])
#     elif t_x[0] == 2:
#         cards.append(t_x[1])
#     else:
#         print(cards[t_x[1]-1])                813msだった。

def main():
    Q = int(input())
    t_x_list = [list(map(int, input().split())) for _ in range(Q)]
    cards = []

    for i in range(Q):
        t_x = t_x_list[i]

        if t_x[0] == 1:
            cards.insert(0, t_x[1])
        elif t_x[0] == 2:
            cards.append(t_x[1])
        else:
            print(cards[t_x[1]-1])

main()                     # 816ms だった。関数無しとほとんど変わらない。差があるときは何なんだ。

