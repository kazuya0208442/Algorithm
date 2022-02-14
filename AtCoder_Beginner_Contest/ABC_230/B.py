# T = 'oxx' * (10 ** 5)
# S = input()

# if S in T:
#     print('Yes')
# else:
#     print('No')






# 周期性を使って解いてみる。oxxoxxoxxoxx....
# 'oxx', 'xxo', 'xox'

S = input()
pattern = ['oxx', 'xxo', 'xox']

for p in pattern:
    for i in range(len(S)):
        if S[i] != p[i%3]:
            break
    else:
        print('Yes')
        exit()

print('No')



