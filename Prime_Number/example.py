from typing import List

def prime_numbers(limit: int) -> List[int]:
    primes = []
    is_prime = [True] * (limit+1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(limit+1):
        if not is_prime[i]:
            continue
        primes.append(i)
        
        for j in range(i*i, limit+1, i):
            is_prime[j] = False
    
    return primes