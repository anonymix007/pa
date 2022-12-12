from sympy import *
x = Symbol('x')
# input n, Q
# output factors, k

n = 5 #
Q = poly(x**40-1, x, modulus=n)

coeff, factors = Q.factor_list()
ans = []
md = 0
for factor in factors:
    ans += [f'({latex(factor[0]/1)})' + (f'^{{{factor[1]}}}' if factor[1]>1 else '')]
    md = max(md, factor[0].degree())
    

print(f'Factors are: {coeff} *', ''.join(ans))

print(f'Minimal field is F_{{{n}}}^{{{md}}} because {md} is max degree of factors')