from sympy import *
x = Symbol('x')
# input n, Q

n = 2
Q = poly('x^11+x^9+x^8+x^4+x^3+x^2+1', x, modulus=n)

roots = Q.ground_roots()
print('Roots are:', roots)

coeff, factors = Q.factor_list()
ans = []
for factor in factors:
    ans += [f'({latex(factor[0]/1)})' + (f'^{{{factor[1]}}}' if factor[1]>1 else '')]

print(f'Factors are: {coeff} *', ''.join(ans))