import heapq

N, K = map(int, input().split())
P = list(map(int, input().split()))
heap = P[:K]

heapq.heapify(heap)

for i in range(K, N+1):
    if i == K:
        min_value = heapq.heappop(heap)
        print(min_value)
        heapq.heappush(heap, min_value)
        continue

    heapq.heappushpop(heap, P[i-1])
    min_value = heapq.heappop(heap)
    print(min_value)
    heapq.heappush(heap, min_value)


