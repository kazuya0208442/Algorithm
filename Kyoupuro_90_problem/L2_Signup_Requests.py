# N = int(input())
# temp = set()
# for i in range(1, N+1):
#  S = str(input())
#  if S in temp: #setだとこの平均計算量がO(1)になる．listだとO(N)
#    continue
#  else:
#    temp.add(S)
#    print(i)             #模範解答 setは重複を防ぐ。




# def main():
#     N = int(input())
#     name_list = [input() for _ in range(N)]
#     name_dict = dict()

#     for index, name in enumerate(name_list):
#         if name in name_dict.keys():
#             continue
#         else:
#             name_dict[name] = index + 1
    
#     # print(*name_dict.values())
#     # print(*name_dict.keys())

#     for i in range(len(name_dict)):
#         print(list(name_dict.values())[i])　　　　# TLEになっちまった・・・

def main():
    N = int(input())
    name_set = set()
    day_num = list()

    for i in range(N):             # in の時はsetが爆速である。ハッシュテーブルがどうとか。
        name = input()

        if name in name_set:
            continue
        else:
            name_set.add(name)
            day_num.append(i+1)

    for j in range(len(day_num)):
        print(day_num[j])

main()
