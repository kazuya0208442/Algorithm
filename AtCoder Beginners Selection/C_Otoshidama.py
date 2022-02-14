


# def main_WA():
#     N, Y_yen = map(int, input().split())

#     if Y_yen % 1000 != 0:               # Y_yen は1000の倍数であると条件で書いてあるので不要だねここ。
#         print(-1, -1, -1)

#     for x in range(N+1):
#         for y in range(N-x+1):
#             for z in range(N-x-y+1):                                #TLE WAだったね。zはx,yが決まると確定するからfor分不要かな。
#                 if 10000 * x + 5000 * y + 1000 * z == Y_yen:
#                     print(x, y, z)
#     print(-1, -1, -1)

# main_WA()


def main():
    N, Y_yen = map(int, input().split())

    for x in range(N+1):
        for y in range(N-x+1):
            z = N - x - y
            if 0 <= z <= 2000 and 10000 * x + 5000 * y + 1000 * z == Y_yen:
                return print(x, y, z)                                               # return にすることで条件に合うものが一つでも来れば終了する。
    print(-1, -1, -1)

main()