# 1 <= N <= 10**9 = 1000000000
# N には 0 でない桁が 2 つ以上含まれることから、max = 999999999  9桁が最高
# N の各桁にbitを用意して、0 or 1 で2つのグループに分けることができる。
# 各桁は２通りの生き方がある。2 ** len(N) 通りの組み合わせがある。
# max でも 2 ** 9 = 512

# import sys

# def main(lines):

#     N = list(map(int, lines[0]))
#     digit = len(N)
#     ans = 0

#     for bit in range(1 << digit):
#         left_number_list = []
#         right_number_list = []
#         for i in range(digit):
#             if (bit >> i) & 1:
#                 right_number_list.append(N[i])
#             else:
#                 left_number_list.append(N[i])

#         if len(left_number_list) == 0 or len(right_number_list) == 0:
#             continue

#         left_number = ''.join(map(str, sorted(left_number_list, reverse=True)))
#         right_number = ''.join(map(str, sorted(right_number_list, reverse=True)))
#         left_number = int(left_number)
#         right_number = int(right_number)

#         ans = max(ans, left_number * right_number)
    
#     print(ans)

# if __name__ == '__main__':
#     lines = []
#     for line in sys.stdin:
#         lines.append(line.rstrip('\r\n'))
#     main(lines)







# 普通に全探索もできる。
# 最大で9桁なので、並び替えは、9! = 362880 通りある。
# さらに、並び変えた後に、仕切り版を入れる箇所は、８か所しかない。
# 730 ms だったわ。bit全探索なら 25 ms よ。やっぱり全探索は時間かかるわ。


import sys
import itertools

def main(lines):

    N_list = list(lines[0])
    digit_sum = len(N_list)
    ans = 0

    for num_list in itertools.permutations(N_list):
        for pertition in range(digit_sum - 1):
            left_number = int(''.join(num_list[:pertition + 1]))
            right_number = int(''.join(num_list[pertition + 1:]))
            ans = max(ans, left_number * right_number)
    
    print(ans)
        
if __name__ == '__main__':
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip('\r\n'))
    main(lines)