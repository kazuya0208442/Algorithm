# from collections import deque


# def main():
#     def make_start():
#         """
#         コマjはP[j]に置かれています。"9"が空きマスということにします
#         str型のリストにしたほうが、後々都合が良いです（''.join(state)で文字列に変換する必要があるため）
#         """
#         start = ["9"] * 9
#         for piece, v in enumerate(P, 1):
#             start[v] = str(piece)
#         return start

#     def bfs(start):
#         def to_str(state):  # setに追加不能なstate: List[str]を、setに追加可能なstrに変換します
#             return ''.join(state)  # いちいちこれを打つのが面倒なため、関数にしておきます

#         goal = [str(i + 1) for i in range(9)]  # ["1", "2", "3", "4", "5", "6", "7", "8", "9"] です
#         seen = set()  # 既に探索した状態を管理します。リストはsetに追加できないので、リストを文字列に変換したものを追加します
#         que = deque()
#         que.append((start, 0))  # 現在のマス目の状態、移動回数

#         while que:
#             state, d = que.popleft()

#             if state == goal:
#                 return d

#             u_empty = state.index("9")  # 空マスの頂点番号を取得し、そこに辺で繋がっている頂点に置いてあるコマを移動させます
#             for v in G[u_empty]:
#                 n_state = state[:]  # 現在の状態をコピーします
#                 n_state[u_empty], n_state[v] = n_state[v], n_state[u_empty]  # # コマを移動します
#                 ns_str = to_str(n_state)  # setで存在判定をするために、strに変換します
#                 if ns_str not in seen:
#                     seen.add(ns_str)
#                     que.append((n_state, d + 1))
#         return -1

#     """
#     コマは1～8の8種類、頂点は-1して、0～8の9頂点とします
#     コマが置かれていない「空の頂点」には、コマ9が置かれていることにします
#     マスの状態は、『頂点i』に『コマj』が置いてある、というリストで管理します
#     """

#     # ここは 入力を受け取って辺から無向グラフを構築しているだけです
#     M = int(input())
#     G = [[] for _ in range(9)]  # 無向グラフです
#     for _ in range(M):
#         u, v = (x - 1 for x in map(int, input().split()))
#         G[u].append(v)
#         G[v].append(u)

#     P = [x - 1 for x in map(int, input().split())]  # Pの中身は頂点番号ですから、それぞれ-1して0はじまりにします
#     start = make_start()  # 最初の盤面の状態を、文字列のリストにして得ます
#     print(bfs(start))


# if __name__ == '__main__':
#     main()



# from collections import deque

# M = int(input())
# route = [[] for _ in range(10)]

# for _ in range(M):
#     u, v = map(int, input().split())
#     route[u].append(v)
#     route[v].append(u)

# P = list(x - 1 for x in map(int, input().split()))   # 9つの頂点番号のインデックスは-1しないとね。
# state = list("9" for _ in range(9))  # ['9', '3', '1', '4', '5', '6', '7', '8', '2']

# for j, pj in enumerate(P, 1):
#     state[pj] = str(j)

# que = deque()
# que.append([state, 0])
# state_set = set()
# goal = [str(i+1) for i in range(9)]

# while que:
#     state, count = que.popleft()

#     if state == goal:
#         print(count)
#         break

#     white = state.index("9") + 1     # 空いてる頂点番号

#     for i in route[white]:
#         state[white-1], state[i-1] = state[i-1], state[white-1]
#         string = ''.join(state)
#         state[white-1], state[i-1] = state[i-1], state[white-1]

#         if string not in state_set:
#             state_set.add(string)
#             que.append([list(string), count+1])

# # print('-1')

# else:
#     print('-1')

