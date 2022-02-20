# 並び替えの総数はN!通り
# N!個の順列をsortすると、O(N!log(N!))
# 順列の長さはNなので、比較するときにN個見るので、全体でO(N*N!log(N!))

import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

permutation = sorted(list(itertools.permutations(range(1, N+1))))

P_num = permutation.index(P) + 1
Q_num = permutation.index(Q) + 1

print(abs(P_num - Q_num))


