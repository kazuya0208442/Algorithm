# 真ん中から決めてあげれば、
# 真ん中よりも小さい数で、かつ、１番右のインデックス
# 真ん中よりも大きい数で、かつ、１番右のインデックス
# を掛け合わせればいい。
# A < B < C

# bisect_leftとbisect_rightの違いは、等号(=)の有無だけで表現できます。
# 条件が x < 5 の時
# 1 2 3 3 3 3 4 4 4 5 5 5 5 6 6 6 6 6 7 8 9 
#                ok|ng 

# 条件が x <= 5 の時
# 1 2 3 3 3 3 4 4 4 5 5 5 5 6 6 6 6 6 7 8 9 
#                        ok|ng 

# N = int(input())
# A = sorted(list(map(int, input().split())))
# B = sorted(list(map(int, input().split())))
# C = sorted(list(map(int, input().split())))
# category_dict = {}

# ans = 0

# for b in B:
#     if category_dict.get(b) != None:
#         ans += category_dict.get(b)
#         continue

#     if A[-1] < b:    # 全てokの時の処理   A(max) < b
#         temp = N
#     elif A[0] > b:   # 全てngの時の処理   A(min) > b
#         category_dict[b] = 0
#         continue
#     else:            # A(min) <= b <= A(max) okとngが初期のカーソルの位置で必ず存在する。
#         left = 0     # 必ずokであることが保証されている。<- ここが違う。b=A[0]の場合、ngである。
#         right = N-1   # 必ずngであることが保証されている。
#         while right - left > 1:
#             mid = (left + right) // 2
#             if A[mid] < b:
#                 left = mid
#             else:
#                 right = mid
#         temp = right
    
#     if b < C[0]:
#         ans += (temp * N)
#         category_dict[b] = temp * N
#     elif b > C[-1]:
#         category_dict[b] = 0
#     else:
#         left = 0
#         right = N-1
#         while right - left > 1:
#             mid = (left + right) // 2
#             if b < C[mid]:
#                 right = mid
#             else:
#                 left = mid
#         ans += (temp * (N-right))
#         category_dict[b] = (temp * (N-right))

# print(ans)
# print(category_dict)





# なんで上の回答が違うのか分かった。コーナーケースを省けていない。不等号のミス


# N = int(input())
# A = sorted(list(map(int, input().split())))
# B = sorted(list(map(int, input().split())))
# C = sorted(list(map(int, input().split())))
# category_dict = {}

# ans = 0

# for b in B:
#     if category_dict.get(b) != None:
#         ans += category_dict.get(b)
#         continue

#     if A[-1] < b:    # 全てokの時の処理   A(max) < b
#         temp = N
#     elif A[0] >= b:   # 全てngの時の処理   A(min) >= b
#         category_dict[b] = 0
#         continue
#     else:            # A(min) <= b <= A(max) okとngが初期のカーソルの位置で必ず存在する。
#         left = 0     # 必ずokであることが保証されている。
#         right = N-1   # 必ずngであることが保証されている。
#         while right - left > 1:
#             mid = (left + right) // 2
#             if A[mid] < b:
#                 left = mid
#             else:
#                 right = mid
#         temp = right
    
#     if b < C[0]:
#         ans += (temp * N)
#         category_dict[b] = temp * N
#     elif b >= C[-1]:
#         category_dict[b] = 0
#     else:
#         left = 0
#         right = N-1
#         while right - left > 1:
#             mid = (left + right) // 2
#             if b < C[mid]:
#                 right = mid
#             else:
#                 left = mid
#         ans += (temp * (N-right))
#         category_dict[b] = (temp * (N-right))

# print(ans)



# 配列の両端にinfを追加するのもありなのかも。
# bisect も使った方がいい。







# 練習で解くよ
# 真ん中の値が５だとする
# 上部は X < 5 を満たす X    4 4 4 4 | 5 5 5   left の条件は X < 5
# 下部は 5 < X を満たす X    5 5 5 5 | 6 6 6   left の条件は X <= 5

import sys
from typing import List

def main(lines: List):
    N = int(lines[0])
    A = sorted(list(map(int, lines[1].split())))
    B = sorted(list(map(int, lines[2].split())))
    C = sorted(list(map(int, lines[3].split())))
    ans = 0

    for b in B:
        if A[-1] < b:
            upper_parts = N
        elif A[0] >= b:
            continue
        else:
            left = 0
            right = N-1
            while right - left > 1:
                mid = (left + right) // 2
                if A[mid] < b:
                    left = mid
                else:
                    right = mid
            upper_parts = right
        
        if b < C[0]:
            ans += upper_parts * N
        elif C[-1] <= b:
            continue
        else:
            left = 0
            right = N-1

            while right - left > 1:
                mid = (left + right) // 2
                if C[mid] <= b:
                    left = mid
                else:
                    right = mid
            ans += upper_parts * (N - right)
    
    print(ans)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)

