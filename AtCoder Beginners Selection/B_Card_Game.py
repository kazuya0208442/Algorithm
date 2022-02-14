# N = int(input())
# a = sorted(map(int, input().split()))[::-1]
# print(sum(a[::2])-sum(a[1::2]))    #模範解答


def main():
    N = int(input())
    card_num = list(map(int, input().split()))
    sorted_card_num = sorted(card_num)
    reversed_sorted_card_num = sorted_card_num[::-1]
    # print(card_num)
    # print(sorted_card_num)
    # print(reversed_sorted_card_num)

    Alice_point = sum(reversed_sorted_card_num[::2])
    Bob_point = sum(reversed_sorted_card_num[1::2])

    dif = Alice_point - Bob_point

    print(dif)

main()










