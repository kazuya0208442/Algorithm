# from typing import List

# def prime_numbers(limit: int) -> List[int]:
#     primes = []
#     is_prime = [True] * (limit+1)
#     is_prime[0] = False
#     is_prime[1] = False

#     for num in range(2, limit+1):
#         if not is_prime[num]:
#             continue
#         primes.append(num)
#         for not_prime_num in range(num**2, limit+1, num):
#             is_prime[not_prime_num] = False
    
#     return primes

# primes = prime_numbers(10**5)
# set_primes = set(prime_numbers(10**5))
# all_nums = [num for num in range(10**5+1)]
# accumulation = [0]

# for i in range(len(all_nums)):
#     if (all_nums[i] in set_primes) and ((all_nums[i]+1)//2 in set_primes):
#         all_nums[i] = 1
#     else:
#         all_nums[i] = 0

# for j in range(len(all_nums)):
#     accumulation.append(accumulation[j]+all_nums[j])


# Q = int(input())

# for _ in range(Q):                      # primeだけのlistだと、累積和のlとrが使えない。10**5のリストで累積和しないと。
#     l, r = map(int, input().split())
#     print(accumulation[r+1] - accumulation[l])    # [l,r+1) の累積和で[l,r]の累積和になる。






# all_nums = [num for num in range(1, 10**5+1)] のように1スタートにすろとWAなのはなぜ？
# a0 をけずったようなもの。何がダメなのだ。
# l と r は現実の数字だから、[1,2,3,4,5,6]の中では,-1が必要だ。
# l と r は現実の数字だから、[0,1,2,3,4,5,6]の中では,-1はいらない！！！。



from typing import List

def prime_numbers(limit: int) -> List[int]:
    primes = []
    is_prime = [True] * (limit+1)
    is_prime[0] = False
    is_prime[1] = False

    for num in range(2, limit+1):
        if not is_prime[num]:
            continue
        primes.append(num)
        for not_prime_num in range(num**2, limit+1, num):
            is_prime[not_prime_num] = False
    
    return primes

primes = prime_numbers(10**5)
set_primes = set(prime_numbers(10**5))
all_nums = [num for num in range(1, 10**5+1)]
accumulation = [0]

for i in range(len(all_nums)):
    if (all_nums[i] in set_primes) and ((all_nums[i]+1)//2 in set_primes):
        all_nums[i] = 1
    else:
        all_nums[i] = 0

for j in range(len(all_nums)):
    accumulation.append(accumulation[j]+all_nums[j])


Q = int(input())

for _ in range(Q):                      # primeだけのlistだと、累積和のlとrが使えない。10**5のリストで累積和しないと。
    l, r = map(int, input().split())
    print(accumulation[r] - accumulation[l-1])    # [l,r+1) の累積和で[l,r]の累積和になる。











