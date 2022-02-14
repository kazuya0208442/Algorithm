# def main():
#     N = int(input())
#     l_v_list = [list(map(int, input().split())) for _ in range(N)]
#     time = 0
#     sum_time = 0
#     time_list = []
#     temp_time = 0
#     temp_length = 0

#     for i in range(N):
#         l_v = l_v_list[i]
#         time = l_v[0] / l_v[1]
#         sum_time += time
#         time_list.append(time)

#     half_time = sum_time / 2

#     for i in range(N):
#         if temp_time + time_list[i] < half_time:
#             temp_time += time_list[i]
#             temp_length += l_v_list[i][0]
#         else:
#             temp_length += l_v_list[i][1] * (half_time - temp_time)
#             break
    
#     print(temp_length)

# main()



N = int(input())
l_v = [tuple(map(int, input().split())) for _ in range(N)]

time = 0
for a, b in l_v:
    time += a / b

half_time = time / 2
s = 0
length = 0

for a, b in l_v:
    s += a / b
    length += a
    if s < half_time:
        continue
    else:
        length -= b * (s - half_time)
        break

print(length)



