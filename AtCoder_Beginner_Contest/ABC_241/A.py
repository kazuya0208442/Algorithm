

ans_list = [0]
numbers = list(map(int, input().split()))
num = 0


for _ in range(3):
    ans_list.append(numbers[num])
    num = numbers[num]

print(ans_list[-1])
