# 優先度付きキュー (Priority queue) はデータ型の一つで、具体的には
# 最小値（最大値）を O(logN)O(log⁡N)で取り出す
# 要素を O(logN)O(log⁡N) で挿入する
# ことが出来ます。通常のリストだとそれぞれ O(N)O(N) ですので高速です。
# 「リストの要素の挿入」と「最小値（最大値）を取り出す」ことを繰り返すような時に使います。



import heapq

N, M = map(int, input().split())
hq = list(map(lambda x: -int(x), input().split()))

heapq.heapify(hq)

for _ in range(M):
    target = heapq.heappop(hq)
    target = -(-target // 2)         # 負の値だから切り上げないとね。
    heapq.heappush(hq, target)

print(-sum(hq))








