# N = int(input())
# A = {tuple(map(int, input().split())) for _ in range(N)}

# print(len(A))


# setに数列をtupleで入れていく。immutableのものしかsetに入らない。
# 唯一のものは、uniqueness とするといいかも。

N = int(input())
uniqueness = set()
num_length = []

for _ in range(N):
    L, *nums = map(int, input().split())
    num_length.append(L)
    uniqueness.add(tuple(nums))

print(len(uniqueness))











