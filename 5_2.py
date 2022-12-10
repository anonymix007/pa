from sympy import *


x = Symbol('x')
a = Symbol('a')

# input coeff mod n, Q, k
# output f

#'''
n = 5 #
k = 3 #
Q = poly(x**2+x+2, x, modulus=n) #
'''
n = 2
k = 7
Q = poly(x**4+x**3+1, x, modulus=n) #
#'''
maxpow = n**Q.degree() - 1

print(f'All coefficients are mod {n}')

pows = []

while k not in pows:
    pows += [k]
    k = (k*n) % maxpow
    # k *= n
    # if (k >= maxpow): break
    
print(f'Max power is {maxpow}')
roots = [f'a^{{{p}}}' for p in pows]

print('Roots are', ', '.join(roots))

p = poly(1, x, a, modulus=n)

for apow in pows:
    p *= poly(x-a**apow, x, a, modulus=n)
print('Min poly is', latex(p/1));
xpoly = {}

x_coeffs = {}
for px, pa in p.monoms():
     if px in x_coeffs:
         x_coeffs[px] += [pa]
     else:
         x_coeffs[px] = [pa]
print('Coefficients in min poly:', x_coeffs)
for px, pa in p.monoms():
    if px in xpoly:
        xpoly[px] += poly(x**pa, x, modulus=n)
    else:
        xpoly[px] = poly(x**pa, x, modulus=n)
print('Simplify coefficients:')

f = poly(0, x, modulus=n)

for px in xpoly.keys():    
    newp = rem(xpoly[px], Q)
    print(f'x^{{{px}}}:', str(latex(xpoly[px].replace(x,a)/1)).ljust(len(pows)*(7*(maxpow+9)//20 + 5)), 'mod Q is', newp/1 % n)

    if newp.degree() > 0:
        print(f'Error! Degree of {latex(xpoly[px]/1)} should be zero!')
    f += poly(newp * x**px, x, modulus=n)
print('\nAnswer:', latex(f/1))
