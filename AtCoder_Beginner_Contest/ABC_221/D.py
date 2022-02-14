

N = int(input())
events = []
count_list = [0 for _ in range(N+1)]
count = 0

for _ in range(N):
    a, b = map(int, input().split())
    events.append([a, 1])
    events.append([a+b, -1])

sorted_ev = sorted(events)
# print(sorted_ev)

for i in range(len(sorted_ev)):
    if i+1 < len(sorted_ev):
        days = sorted_ev[i+1][0] - sorted_ev[i][0]
        count += sorted_ev[i][1]
        count_list[count] += days

print(*count_list[1:])


