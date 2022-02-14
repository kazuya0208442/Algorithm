# f(9) = 1,2,3,...9             9      f(7) = 7 (- 1 + 1)  
# f(99) = 10,11,12,...99        90     f(16) = 16 (- 10 + 1)
# f(999) = 100,101,...999       900    f(367) = 367 (- 100 + 1)

# (1+2+3+..9)   -9*0
# (10+11+,,,99) -9*1*90
# (100+101+...999) - 9*11*900

# f(367)
# f(1)+...f(99)

# n(a+l)//2


N = int(input())
mod = 998244353
ans = 0

def acuumulation_count(x: int) -> int:
    x = str(x)
    digit_count = len(x)-1
    ans = 0
    for i in range(digit_count):
        temp = ((10**(i+1) - 10**i) * (10**i + 10**(i+1) - 1)//2) + ((1-10**i)*9*10**i)
        ans += temp
        ans %= mod
    return ans



def lower_count(x: int) -> int:
    x = str(x)
    digit_count = len(x)
    x = int(x)
    ans = 0

    for i in range(10**(digit_count-1), x+1):
        ans += ((i - 10 ** (digit_count-1)) + 1)
        ans %= mod
    
    return ans
        


 

ans += acuumulation_count(N)
ans += lower_count(N)
ans %= mod

print(ans)






