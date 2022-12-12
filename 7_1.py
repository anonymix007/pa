from sympy import *
import sys
stdout_fileno = sys.stdout


def get_simplification(ais, si):
    if si in ais: 
        return ais[si]
    for key in ais.keys():
        const, rem = div(key, si)
        if rem == 0 and const.degree() == 0:
            return const * ais[key]
            
def simplify_xpoly(xpoly, p):
    result = poly(0, x, modulus=n)
    for term in xpoly.all_terms():
        newt = poly(term[1]*x**(term[0][0] % p), x, modulus=n)
        result += newt
    return result
    
def simplify_axpoly(axpoly, p):
    result = poly(0, x, modulus=n)
    for coeff, (px, pa) in zip(axpoly.coeffs(), axpoly.monoms()):
        newt = poly(coeff* x**px * a ** (pa % p), x, a, modulus=n)
        #print(coeff, px, pa, latex(newt/1))
        result += newt
    #print(result)
    return result  

def xgcd(rm2, rm1, ym2, ym1, i, r, p):
    
    q0 = pquo(rm2, rm1, gens=[x,a])
    r0 = prem(rm2, rm1, gens=[x,a])
    
    q0 = simplify_axpoly(q0, p)
    r0 = simplify_axpoly(r0, p)

    quot, rema = div(rm2, simplify_axpoly(rm1*q0+r0, p))
    
    q0 = simplify_axpoly(q0*quot, p)
    r0 = simplify_axpoly(r0*quot, p)
    
    #assert(rema == 0)    
    
    y0 = ym2 - ym1 * q0
    y0 = simplify_axpoly(y0, p)
    print(f'#{i+1}\n    r_{{{i-2}}} = r_{{{i-1}}} * q_{{{i}}} + r_{{{i}}}')
    print('    ', latex(rm2/1), '=')
    print(f'    r_{{{i}}} =', latex(r0/1), f'\n    q_{{{i}}} =', latex(q0/1))
    print(f'    y_{{{i}}} = y_{{{i-2}}} - y_{{{i-1}}} * q_{{{i}}} =', latex(y0/1))
    
    if r0.degree() <= r:
        return y0#quo(y0, r0)
    
    return xgcd(rm1, r0, ym1, y0, i+1, r, p)

x = Symbol('x')
a = Symbol('a')

# input n, r, Q, w
# output s(x)


print('Input n:') 
n = int(input()) #2
print('Input Q:') 
Q = poly(input(), modulus=n) #x**4+x+1
print('Input r:')
r = int(input()) #2
print('Input w:') 
w = poly(input(), modulus=n)# x**14+x**10+x**5+x**4

m = Q.degree()
p = n**m - 1
sys.stdout = open('out/7_1.txt', 'w')
print(f'Simplify powers of a (from 1 to {p})')

ais = {}

for i in range(1, p + 1):
    simpl = rem(poly(x**i, x, modulus=n), Q)
    ais[simpl] = poly(x**i, x, modulus=n)
    print(f'a^{{{i}}}'.ljust(10), '|', latex(simpl.replace(x, a)/1))

print(f'Calculating {2 * r} syndroms')

sis = []
rm1 = poly(1, x, a, modulus=2);
for i in range(1, 2 * r + 1):
    siss = []
    if (i % 2 == 0):
        siss += [sis[(i-1)//2]**2]
        print(f's_{{{i}}} = (s_{{{i//2}}})^2 = ', end='')
    else:
        siss += [poly(w.as_expr(x**i), x, modulus=n)]
        print(f's_{{{i}}} = w(a^{{{i}}}) = ', end='')
    #siss += [poly(0, x, modulus=n)]
    siss += [simplify_xpoly(siss[0], p)]
    #for term in siss[0].all_terms():
    #    newt = poly(term[1]*x**(term[0][0] % p), x, modulus=n)
    #    siss[1] += newt
    if len(siss[1].coeffs()) > 1:
        siss += [rem(siss[1], Q)]
        if len(siss[2].coeffs()) > 1:
            siss += [get_simplification(ais, siss[2])]
    sis += [siss[len(siss)-1]]
    ltx = {}
    for j, si in enumerate(siss):
        if not latex(si/1) in ltx:
            ltx[latex(si.replace(x, a)/1)] = j
        if len(si.coeffs()) <= 1 and si.degree() < p: break
    #print(ltx)
    print(' = '.join(ltx.keys()))
    rm1 += poly(sis[i-1].replace(x,a).as_expr() * x**i, x, a, modulus=2)

rm2 = poly(a**p*x**(2*r+1), x, a, modulus=2)

print('Syndrome polynomial is', latex(rm1/1))

print('#0\n    r_{-2} =', latex(rm2/1))
print('    r_{-1} =', latex(rm1/1))
print('    y_{-2} = 0\n    y_{-1} = 1')
ym2 = poly(0, x, modulus=n)
ym1 = poly(1, x, modulus=n)

s = xgcd(rm2, rm1, ym2, ym1, 0, r, p)
#s = gcdex(rm2, rm1)
print('CAUTION: multivariate polynomial division is too hard, so this uses dirty hack!')

print(f'\nAnswer: s(x) =', latex(s/1))

sys.stdout.close()
sys.stdout = stdout_fileno

print('File written')
