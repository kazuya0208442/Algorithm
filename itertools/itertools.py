import itertools

# list in list になっている、袋の中のボールを一つずつ取り出すときに便利。

[v for v in itertools.product(*[[1,2,3],[4,5,6]], repeat=1)]

# [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]