# print 改行有り無しとか
# format関数
# print(str(29).rjust(10,'0')) #10桁ゼロ埋め string メソッド
# 0000000029

# import bisect
# listA=[1,2,5,2,4,6,7,8,6,56,3,56,76,34,32,2,6,0,32,6,0,...] 
# listA.sort()
# zeroindex=bisect.bisect_right(listA,0) #ソートされたリスト内で0の場所を探し、右側Indexを返す
# clearlistA=listA[zeroindex:]#0以下が存在しないリストを得る
# 巨大なリストに存在する0以下の数字をすべて簡単に消す必要があるとき

# 'abc123def'[:-1] #最後の1文字以外のものがとれる。
# 'abc123de'

# 'abc123def'[::-1] #文字が逆転する
# 'fed321cba'

# list.index(n)では一致した値のインデックスを一つしか返さない。リスト内包表記を用いて複数の値をリストにまとめて返す。
# li = [0, 2, 1, 4, 2, 3, 2] 
# indexes = [i for i, x in enumerate(li) if x == 2] # 2を検索
# print(indexes) # [1, 4, 6]

# ある区間の和をO(1)O(1)で求めるアルゴリズム。前処理にO(N)O(N)かかる。
# 数列{an}{an}に対してs0=0,si=∑i−1k=0aks0=0,si=∑k=0i−1akを満たす数列{sn}{sn}を定義する。
# つまり、sisiは[0,i)[0,i)の和である。
# [a,b)[a,b)の和がsb−sasb−saで求められる。

#a = [i for i in range(11)]
# s = [0]
# for i in a:
#     s.append(s[-1] + i)
# print(s[3] - s[0]) # 0 + 1 + 2 = 3
# print(s[11] - s[8]) # 8 + 9 + 10 = 27
