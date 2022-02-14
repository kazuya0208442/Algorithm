# x = input('Enter your name:')
# print('Hello, ' + x)


# S = input().split('4')   #inputの実験 split()は各要素をリストにして返してくれる。空白で区切る。28 38 99 99 9 -> ['28', '38', '99', '99', '9']
# print(type(S))
# print(S)

# A = map(int, input().split())   #mapの実験
# print(type(A))
# print(A)

# for i in A:
#     print(i)

# for i in range(0):     # 何も表示されへんのこれだと。
#     print(type(i))

# for i in map(int, str(76543)):     #どうやら'11111'という文字列はiterableらしい。for loopで回せるものはiterableだって。
#     print(i)
# print(list(map(int, str(76543))))
# print(sum(list(map(int, str(76543)))))
# print(sum(map(int, str(76543))))

# for i in 'kakadada112':         #for loopで回せるものはiterableだって。
#     print(i)



# a = []

# for i in a:
#     print(i)
#     break
# else:
#     print('Y')


# print('a', end='')
# print('B')

# A + Bx <= DCx  A <= x(DC-B)  A / (DC-B) <= x
# 2 3^
# 2^ 3 4
# class="content" 

# string = '<iframe width="560" height="315" src="https://www.youtube.com/embed/ZOFO_MzZi50" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'

# index_embed = string.find('embed/')

# first_str = string[:index_embed + 17]
# second_str = 'aaaaa'
# last_str = string[index_embed + 17:]

# new_str = '<div class="wrapper"> ' + first_str + second_str + last_str + ' </div>'

# print(new_str)

# S = list(input())
# print(S, type(S))

# V = [1,2,4,5]
# V = list(map(str, V))
# S = ''.join(V)      # join は文字列のみ結合可能。intはダメ。
# print(S)


# nums = [1,2,3,3,4,4,5,5,5,5,7,7,8,89,9,0,1,2,3,4,5]  # 現れたindexをlistのして保存
# dict = {}

# for i in range(len(nums)):

#     dict[nums[i]] = dict.get(nums[i], list())   # keyがなかったら、新たにkeyとvalue(空のリスト)を追加する。
#     dict[nums[i]].append(i)

# print(dict)



N, Q = map(int, input().split())
a = list(map(int, input().split()))
dict = {}

for i in range(N):
    dict[a[i]] = dict.get(a[i], [])
    dict[a[i]].append(i)

for j in range(Q):
    x, k = map(int, input().split())

    if x in dict.keys() and k <= len(dict[x]):
        # print(dict[x])
        print(dict[x][k-1]+1)
    else:
        print(-1)
