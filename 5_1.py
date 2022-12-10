from sympy import *


x = Symbol('x')
a = Symbol('a')

# input coeff mod n, Q
# output f

n = 3
Q = poly(x**3+x+2, x, modulus=n) #

roots = Q.ground_roots() # {root : multiplicity
A, factors = Q.factor_list()

print(f'Factorization in F_{{{n}}} is ' + (f'{A} *' if A > 1 else '') + '*'.join([f'({latex(f[0]/1)})' + (f'**{f[1]}' if f[1]>1 else '') for f in factors]))

nonlinears = [factor[0] for factor in factors if factor[0].degree() > 1]
powers = [factor[1] for factor in factors if factor[0].degree() > 1]

ans = [str(key%n) for key in roots.keys()]

#for g, power in zip(nonlinears, powers):
assert(len(nonlinears) == len(powers) == 1)

g = nonlinears[0]
power = powers[0]
print('g(x) = ', latex(g/1), f'to the power of {power}') 
print(f'Consider field F_{{{n}}}/((g(x)))')
groot_powers = [n**s for s in range(g.degree())]
print(f'Powers of roots {groot_powers}')
for gp in groot_powers:
    root = rem(poly(x**gp, x, modulus=n), Q)
    print(f'Root a^{{{gp}}} is now', str(latex(root.replace(x, a) / 1)))
    ans += [latex(root/1)]
# For loop should end here. No idea how to handle multiple irreducible polynomials
ans = ', '.join(ans)
print(f'\nAnswer: roots are {ans} (multiplicities are ignored) in F_{{{n}}}/({latex(g/1)}) ')
'''
maxpow = n**Q.degree() - 1

pows = []

while k not in pows:
    pows += [k]
    k = (k*n) % maxpow
    # k *= n
    # if (k >= maxpow): break
    
print(f'Max power is {maxpow}')
roots = [f'a^{{{p}}}' for p in pows]
print(f'Roots are {roots}')

p = poly(1, x, a, modulus=n)

for apow in pows:
    p *= poly(x-a**apow, x, a, modulus=n)
print('Min poly is', p);
xpoly = {}

test = {}
for px, pa in p.monoms():
     if px in test:
         test[px] += [pa]
     else:
         test[px] = [pa]
print('powers test', test)
for px, pa in p.monoms():
    if px in xpoly:
        xpoly[px] += poly(x**pa, x, modulus=n)
    else:
        xpoly[px] = poly(x**pa, x, modulus=n)
print('Simplify coefficients:')

f = poly(0, x, modulus=n)
print(xpoly)

for px in xpoly.keys():    
    newp = rem(xpoly[px], Q)
    print(f'x**{px}:', str(xpoly[px]/1).replace('x**', 'a**').ljust(len(pows)*((maxpow+9)//10 + 5)), 'mod Q is', newp/1 % n)

    if newp.degree() > 0:
        print(f'Error! Degree of {xpoly[px]} should be zero!')
    f += poly(newp * x**px, x, modulus=n)
print('\nAnswer:', f)
'''
