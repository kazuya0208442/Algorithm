# N, K = map(int, input().split())
# P = [[sum(list(map(int, input().split()))), i] for i in range(N)]
# P_sorted = sorted(P, reverse=True)
# border = P_sorted[K - 1][0]
# judge = [False] * N
# # print(P)
# # print(border)


# for i in range(N):
#     if i < K:
#         judge[P_sorted[i][1]] = True

#     elif border - P_sorted[i][0] <= 300:
#         judge[P_sorted[i][1]] = True

# for j in range(N):
#     if judge[j]:
#         print('Yes')
#     else:
#         print('No')




# 既にK位以内であれば、Yes
# K位の点数がborderになる。300点を足して、K位の点数以上の点数が取れるのならYes

N, K = map(int, input().split())
points = []
students = [False] * (N+1)

for i in range(N):
    point_3days = list(map(int, input().split()))
    points.append([sum(point_3days), i+1])

points.sort(reverse=True)
border_point = points[K-1][0]

for i, list in enumerate(points):
    sum_3days_points = list[0]
    student_num = list[1]
    if i+1 <= K:
        students[student_num] = True
    elif sum_3days_points + 300 >= border_point:
        students[student_num] = True

for j in range(1, N+1):
    if students[j]:
        print('Yes')
    else:
        print('No')



