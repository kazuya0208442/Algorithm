# old: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
# new: [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# newで[22, 6, 24, 23]をsortしたいときは、oldでの強さランキングみたいな index = [3, 19, 1, 2] これを並べ替える。
# ans = [1, 2, 3, 19] = [24, 23, 22, 6]
# これのアルファベット順バージョンを作ろう。
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']


X = list(input())
N = int(input())
S = [list(input()) for _ in range(N)]
A = [chr(ord("a")+i) for i in range(26)]

def now_to_base(now, base, target):
    for i in range(len(target)):
        n = len(target[i])
        string = target[i]
        for j in range(n):
            string[j] = base[now.index(string[j])]
    return target

S_new = sorted(now_to_base(X, A, S))
ans_list = now_to_base(A, X, S_new)

for j in range(len(ans_list)):
    print(''.join(ans_list[j]))








        





