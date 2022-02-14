

N = int(input())
route = [int(input()) for _ in range(N-1)]
in_deg = [0] * (N+1)

for i in range(N-1):
    in_deg[route[i]] += 1

print(in_deg)
