import string


S = list(input())
alphabet = string.ascii_lowercase
numbers = '0123456789'
ans = {v:0 for v in alphabet}
# count = 0
nums = []
product = 1
temp_num = ''

for i in range(len(S)):
    if S[i] in alphabet:
        if temp_num:
            ans[S[i]] += int(temp_num) * product
            temp_num = ''
        else:
            ans[S[i]] += product

    elif S[i] in numbers:
        temp_num += S[i]

    elif S[i] == '(':
        product *= int(temp_num)
        nums.append(int(temp_num))
        temp_num = ''
        # count += 1
    else:
        product //= int(nums.pop())

for v, count in ans.items():
    print(v, count)
    
        











