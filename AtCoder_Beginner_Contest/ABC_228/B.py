# N, X = map(int, input().split())
# A = list(map(int, input().split()))
# known = [False] * (N+1)
# known[X] = True
# num = X-1


# while not known[A[num]]:
#     known[A[num]] = True
#     num = A[num] - 1

# ans = known.count(True)
# print(ans)





# フラグを立てていき、過去にフラグを立てていた人に当たった場合終了。

N, X = map(int, input().split())
friends = list(map(int, input().split()))
is_exposed = [False] * (N+1)

while not is_exposed[X]:
    is_exposed[X] = True
    X = friends[X-1]

print(sum(is_exposed))










