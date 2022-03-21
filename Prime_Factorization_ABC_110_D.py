# 素因数分解して、各素因数は、N個のグループの中から、１つ選べる。
# N ** (素因数の総数) が答え？

# 12 = 2**2 + 3**1      N = 3の時
# 5! / 2!2! = 5*3*2

# ((素因数の総数) + (N-1)[仕切りの数のこと])! / 重複する素因数と仕切りの階乗



# フェルマーの小定理が必要なため、この問題は飛ばす！！！
# 素因数分解だけやる。
# N**(1/2)以下の素数を列挙して、辞書型で、素因数がそれぞれいくつあるのかを列挙する。

# from typing import Dict , List
# from collections import defaultdict

# def prime_number(N: int) -> List[int]:
#     prime_nums = []
#     is_prime = [True] * (N+1)
#     is_prime[0] = False
#     is_prime[1] = False

#     for num in range(2, N+1):
#         if is_prime[num]:
#             prime_nums.append(num)

#             for v in range(num*num, N+1, num):
#                 is_prime[v] = False
    
#     return prime_nums


# def prime_factorization(N: int) -> Dict[int, int]:
#     prime_fact_dict = defaultdict(int)
#     # upper_limit = int(pow(N, 1/2))
#     # prime_nums = prime_number(upper_limit)
#     prime_nums = prime_number(N)

#     for prime in prime_nums:
#         while N and N % prime == 0:
#             prime_fact_dict[prime] += 1
#             N //= prime
    
#     return prime_fact_dict

# print(prime_factorization(97937))
# print(prime_number(97937))








# 素因数分解の練習
from typing import List, Dict
from collections import defaultdict
import sys

def main(lines: List):
    def prime_generation(N: int) -> List[int]:
        primes = []
        is_prime = [True] * (N+1)
        is_prime[0] = False
        is_prime[1] = False

        for number in range(2, N+1):
            if is_prime[number]:
                primes.append(number)
            else:
                continue

            for v in range(number ** 2, N+1, number):
                is_prime[v] = False
            
        return primes
    
    def prime_factorization(N: int) -> Dict[int, int]:
        primes = prime_generation(N)
        prime_factorization_dict = defaultdict(int)

        for prime in primes:
            while N and N % prime == 0:
                prime_factorization_dict[prime] += 1
                N //= prime
        
        return prime_factorization_dict
    
    N = int(lines[0])
    # print(prime_generation(N))
    print(prime_factorization(N))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)


