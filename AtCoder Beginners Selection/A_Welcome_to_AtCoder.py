"""
問題文
高橋君はデータの加工が行いたいです。

整数 a,b,cと、文字列 s が与えられます。 a+b+c の計算結果と、文字列 s を並べて表示しなさい。

制約
1≤a,b,c≤1,000
1≤∣s∣≤100
"""

# -*- coding: utf-8 -*-
# 整数の入力
a = int(input())             
# スペース区切りの整数の入力
b, c = map(int, input().split())   #map() input().split()はlistで、各値にint()を作用させる。split()はデフォルトで空白文字を区切りにして、それぞれをlistに入れて返す。
# 文字列の入力
s = input()
# 出力
print("{} {}".format(a+b+c, s))

