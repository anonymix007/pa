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

# input n, r, Q, w
# output dec(x)

n = 2
Q = poly(x**3+x+1, modulus=n)
w = poly(x**7+x**6+x**2+1, modulus=n)

m = Q.degree()
p = n**m - 1

print(f'Simplify powers of a (from 1 to {p})')

ais = {}

for i in range(1, p + 1):
    simpl = rem(poly(x**i, x, modulus=n), Q)
    ais[simpl] = poly(x**i, x, modulus=n)
    print(f'a^{{{i}}}'.ljust(10), '|', latex(simpl.replace(x, a)/1))
    
roots = []

s = rem(w, Q)
k = get_simplification(ais, s).degree() % p
err = poly(x**k, x, modulus=n)
v = w + err
print('s = w(a) =', latex(w.replace(x, a)/1), '=', latex(s/1), '=> k =', k)
print('v(x) = w(x) + e(x) =', latex(v/1)) 
