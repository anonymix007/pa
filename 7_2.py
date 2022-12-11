from sympy import *


def get_simplification(ais, si):
    if si in ais: 
        return ais[si]
    for key in ais.keys():
        const, rem = div(key, si)
        if rem == 0 and const.degree() == 0:
            return const * ais[key]

x = Symbol('x')
a = Symbol('a')

# input n, r, Q, s
# output err(x)

n = 2
Q = poly(x**4+x+1, modulus=n)
r = 2
s = poly(a**2*x**2+a**6*x+1, modulus=n)

m = Q.degree()
p = n**m - 1

print(f'Simplify powers of a (from 1 to {p})')

ais = {}

for i in range(1, p + 1):
    simpl = rem(poly(x**i, x, modulus=n), Q)
    ais[simpl] = poly(x**i, x, modulus=n)
    print(f'a^{{{i}}}'.ljust(10), '|', latex(simpl.replace(x, a)/1))
    
roots = []

for i in range(1, p + 1):
    sai = poly(s.as_expr({x:a**i}).replace(a, x), x, modulus=n)
    newsai = poly(0, x, modulus=n)
    for term in sai.all_terms():
        newt = poly(term[1]*x**(term[0][0] % p), x, modulus=n)
        newsai += newt
    newsai = rem(newsai, Q)
    print(f's(a^{{{i}}}) =', latex(newsai.replace(x, a)/1), end=' ')
    if newsai.degree() < 1:
        if newsai == 0:
            roots += [i]
        print()
    else:
        print('=', latex(get_simplification(ais, newsai).replace(x, a)/1))

print('Powers of roots are', roots)

err = poly(0, x, modulus=n)
for root in roots:
    err += poly(x**(p-root), x, modulus=n)

print(f'\nAnswer: err(x) =', latex(err/1))
