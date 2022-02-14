import itertools

S, K = input().split(' ')
S = list(S)
K = int(K)
ans_set = set()

for i in  itertools.permutations(S):
    ans_set.add(i)

ans_list = sorted(list(ans_set))

print(''.join(ans_list[K-1]))







