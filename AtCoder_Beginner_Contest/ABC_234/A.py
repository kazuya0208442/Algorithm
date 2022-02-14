# t = int(input())

# def f(x):
#     return x**2 + 2*x + 3

# ft = f(t)
# ft_t = ft + t
# f_ft_t = f(ft_t)
# f_ft = f(ft)
# ans = f(f_ft_t + f_ft)

# print(ans)





# 丁寧に解いてみる

def calc(x: int) -> int:
    return x**2 + 2*x + 3

t = int(input())

print(calc(calc(calc(t) + t) + calc(calc(t))))
