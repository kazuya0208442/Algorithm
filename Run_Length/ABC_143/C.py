N = int(input())
S = list(input())
merged_slime = []

for i in range(N):
    if (len(merged_slime) == 0) or merged_slime[-1] != S[i]:
        merged_slime.append(S[i])

print(len(merged_slime))