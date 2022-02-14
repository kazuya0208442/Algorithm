# 1,0をカウントして、0が２回来たら１のカウントをリセット、１が５より大きくなるとアウト。これだとあかん、途中から条件満たすときあるし。



# def main():
#     N = int(input())
#     work_sch = list(map(int, input().split()))
#     work_count = 0
#     holiday_count = 0
#     day_num = 0

#     for i in range(N):
#         if work_sch[i] == 1:
#             work_count += 1
#         else:
#             holiday_count += 1

#         if work_count > 5 and holiday_count < 2:
#             return print(day_num)
        
#         if holiday_count == 2:
#             day_num = i+1
#             work_count = 0
#             holiday_count = 0
    
#     print(N)

# main()

# def main():
#     N = int(input())
#     work_sch = list(map(int, input().split()))
#     start = []
#     check = True

#     for i in range(N-6):
#         seven_day = work_sch[i:i+7]
#         if seven_day.count(0) < 2 and check == True:
#             continue
#         elif seven_day.count(0) >= 2:
#             check = False
#             start.append(i)
#         else:
#             break
#     if len(start) == 0:
#         return print('0')
#     elif len(start) == 1:
#         return print('7')
#     ans = start[-1] + 7 - start[0]

#     print(ans)
        
# main()


N = int(input())
days = list(map(int, input().split()))
check = [0] * (N - 7 + 1)
count = 6
ans = {6}

for i in range(N - 7 + 1):
    if days[i:i+7].count(0) >= 2:
        check[i] = 1
# print(check)

for j in range(len(check)):
    if check[j] == 1:
        count += 1
    else:
        ans.add(count)
        count = 6

ans.add(count)
# print(ans)
if max(ans) == 6:
    print('0')
else:
    print(max(ans))


            


        


