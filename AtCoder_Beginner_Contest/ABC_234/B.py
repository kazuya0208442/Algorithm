# N = int(input())
# xy = [list(map(int, input().split())) for _ in range(N)]
# ans = 0

# def length(a, b):
#     x1, y1 = a
#     x2, y2 = b
#     return (abs(x1-x2)**2 + abs(y1-y2)**2)**(1/2)



# for i in range(N-1):
#     for j in range(i+1, N):
#         ans = max(length(xy[i], xy[j]), ans)

# print(ans)


N = int(input())
x_y_list = [list(map(int, input().split())) for _ in range(N)]
ans = 0

def calc_length(x1: int, y1: int, x2: int, y2: int) -> int:
    x_diff = x1 - x2
    y_diff = y1 - y2
    return (x_diff**2 + y_diff**2)**(1/2)

for i in range(N):
    for j in range(i+1, N):
        x1, y1 = x_y_list[i]
        x2, y2 = x_y_list[j]
        ans = max(ans, calc_length(x1, y1, x2, y2)) 

print(ans)