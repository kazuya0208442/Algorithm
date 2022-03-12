import sys

def main(lines):
    Q = int(lines[0])
    max_num = 10**5 + 1
    like_2017_numbers = [0] *  max_num

    prime_condition = [True] *  max_num
    prime_condition[0] = False
    prime_condition[1] = False

    for num in range(2,  max_num):
        if not prime_condition[num]:
            continue

        for v in range(num**2, max_num, num):
            prime_condition[v] = False
    
    for num in range(max_num):
        if prime_condition[num]:
            if prime_condition[(num + 1) // 2]:
                like_2017_numbers[num] += 1
    
    accumuration = [0]
    ans = []

    for i in range(max_num):
        accumuration.append(accumuration[i] + like_2017_numbers[i])
    
    for row in lines[1:]:
        l, r = map(int, row.split())
        ans.append(accumuration[r+1] - accumuration[l])
    
    for v in ans:
        print(v)



if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)