

N, M = map(int, input().split())
nudle_length = list(map(int, input().split()))
needed_nudle_length = list(map(int, input().split()))
nudle_length_dict = {}

for length in nudle_length:
    nudle_length_dict[length] = nudle_length_dict.get(length, 0) + 1

for v in needed_nudle_length:
    if (nudle_length_dict.get(v) is None) or (nudle_length_dict.get(v) == 0):
        print('No')
        exit()
    nudle_length_dict[v] -= 1

print('Yes')
    






