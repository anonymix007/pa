from sympy import *
from sympy.polys.agca.extensions import FiniteExtension

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

# This should theoretically work, but it rather gives NotImplementedError.
# F = FiniteExtension(g)
# newQ = poly(Q.as_expr(), x, domain=F)
# print(newQ.factor_list())
# print(newQ.ground_roots())
# Loop should be: over all non-linear add new extension into domain, after loop call factor_list() or ground_roots()
# Or not...
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
