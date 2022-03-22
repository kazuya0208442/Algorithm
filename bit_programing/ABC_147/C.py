# # 先にN人の0 or 1を決めておく。後は、1の証言だけが正しいので、１の証言と、あらかじめ決めた0or1が一致しているかを見る。


# N = int(input())
# testimony = []
# ans = 0

# for _ in range(N):
#     A = int(input())
#     temp = [list(map(int, input().split())) for _ in range(A)]
#     testimony.append(temp)


# # print(testimony)

# for i in range(1 << N):
#     true_false_list = []
#     for j in range(N):
#         if (i >> j) & 1:
#             true_false_list.append(1)
#         else:
#             true_false_list.append(0)
#     out = False
#     for k in range(N):
#         if true_false_list[k] == 1:
#             for person_num, bit in testimony[k]:
#                 if true_false_list[person_num-1] != bit:
#                     out = True
#                     break
#             if out:
#                 break
#     else:
#         ans = max(ans, sum(true_false_list))


# print(ans)





# 練習するぜ
# bit を最後の桁から見ていくので、最後の人の証言から検証していくように for x, y in testimony[N-1-i]: ってやってる。
# bin(8) = '0b1000' とかになるので、初めの２文字は削ればいい。


import sys
from typing import List

def main(lines: List):
    N = int(lines[0])
    pointer = 1
    testimony = [[] for _ in range(N)]
    out = False
    ans = 0

    for i in range(N):
        A = int(lines[pointer])
        for _ in range(A):
            pointer += 1
            x, y = map(int, lines[pointer].split())
            testimony[i].append([x, y])
        pointer += 1
    
    # print(testimony)

    for bit in range(1 << N):
        bit_list = list(map(int, list('0' * N + bin(bit)[2:])[-N:]))
        # print(bit_list)
        for i in range(N):
            if (bit >> i) & 1:
                for x, y in testimony[N-1-i]:
                    if bit_list[x-1] != y:
                        out = True
                        break
            if out:
                out = False
                break
        else:
            ans = max(ans, sum(bit_list))
    
    print(ans)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)

