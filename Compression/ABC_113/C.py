# あんまりよくない方法かも。面倒かも。
# まずは県の配列を作って、そこに、[市の番号, 年]を追加
# 県を一つずつ見ていって、二番目の値でsortする
# dictを作って、各年に対応する順位をenumerateでやる。リストが取れるから、1番目の要素を指定
# [市の番号, 年] -> [市の番号, 順位]に書き換え。
# その後、もう一度県を全探索して、県番号と順位を使って識別番号を作成して、dictに代入した。



N, M = map(int, input().split())
prefecture = [[] for _ in range(N+1)]
ans = {}

for i in range(1, M+1):
    P, Y = map(int, input().split())
    prefecture[P].append([i, Y])

for j in prefecture:
    if len(j) == 0:
        continue
    j.sort(key=lambda x: x[1])
    # print(j)
    dict = {v[1]: i+1 for i, v in enumerate(j)}
    for k in j:
        k[1] = dict[k[1]]
    
# print(prefecture)

for i in range(1, N+1):
    for city_num, order in prefecture[i]:
        prefecture_num = ('0' * 5 + str(i))[-6:]
        order_num = ('0' * 5 + str(order))[-6:]
        auth_num = prefecture_num + order_num
        dict[city_num] = auth_num

for j in range(1, M+1):
    print(dict[j])






# 市の番号と順位さえ分かれば、識別番号はできるから、その時点でansのdictに突っ込んでいい。









