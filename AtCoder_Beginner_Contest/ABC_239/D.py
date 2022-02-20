# Takahashiが勝つには、足されても素数にならない数が１つでもあればいい
# iを決めて、jが全部回っても素数にできないなら、そのiを出せば高橋の勝ち

from typing import Set

def make_prime_number(N: int) -> Set[int]:
    prime_nums = set()
    is_prime = [True] * (N+1)
    is_prime[0] = False
    is_prime[1] = False

    for num in range(2, N+1):
        if is_prime[num]:
            prime_nums.add(num)

        for v in range(num*num, N+1, num):
            is_prime[v] = False

    return prime_nums

A, B, C, D = map(int, input().split())
prime_nums = make_prime_number(B+D)

for i in range(A, B+1):
    for j in range(C, D+1):
        if (i+j) in prime_nums:
            break
    else:
        print('Takahashi')
        exit()

print('Aoki')








