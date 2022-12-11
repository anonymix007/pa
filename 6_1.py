from sympy import *


def poly_to_bin(polynomial, length):
    coeffs = polynomial.all_terms()
    coeffs = [(0,0)]*(length - len(coeffs)) + coeffs
    coeffs.reverse()
    return [str(b[1]) for b in coeffs]

x = Symbol('x')
a = Symbol('a')

# input m, n, g, u
# output d, f (=encoded u)

#'''
m = 7 #
n = 3 #
g = poly(x**4+x**3+x**2+1, x, modulus=2) #
u = poly(x**2+1, x, modulus=2) #
'''

#'''
k = g.degree()

f = u * poly(x**k, modulus=2)

rowlen = n

print(f'All coefficients are mod {2}')
print(f'Code is ({m}, {n}), so {m} bits in encoded words, {n} bits in to-be-coded words')
print(f'Bruteforce {n} coefficients, total {2**n - 1} combinations')
print('val'.ljust(rowlen), '|', ' '.join([str(kv) for kv in range(m)]), '| N')
d = m
for v in range(1, 2**n):
    s = format(v, f'0{n}b')
    
    coeffs = [ord(c)-ord('0') for c in s]
    coeffs.reverse()
    Q = poly(0, x, modulus=2)
    for i, c in enumerate(coeffs):
        if c == 1:
            Q += poly(c*x**i, x, modulus=2)
    v = g*Q
    N = len(v.coeffs())
    d = min(d, N)
    print(s.ljust(rowlen),  '|', ' '.join(poly_to_bin(v, m)), '|', N)

print(f'Code distance is min(N) = {d}')
print(f'Encoding is done via f = u x^{{{k}}} + r, where r is (u x^{{{k}}}) mod g(x), r(x) =', latex(rem(f,g)/1))
f = f + rem(f, g)
enc = ''.join(poly_to_bin(f, m))
print('f =', latex(f/1), f'or {enc} in binary')

print(f'\nAnswer: distance is {d}, encoded polynomial is {enc}')

