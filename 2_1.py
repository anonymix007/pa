from sympy import *
import sys
stdout_fileno = sys.stdout

def xgcd(rm2, rm1, ym2, ym1, i):
    
    q0 = quo(rm2, rm1)
    r0 = rem(rm2, rm1)
    y0 = ym2 - ym1 * q0
    
    print(f'#{i+1}\n    r_{{{i-2}}} = r_{{{i-1}}} * q_{{{i}}} + r_{{{i}}}')
    print(f'    r_{{{i}}} =', latex(r0/1), f'\n    q_{{{i}}} =', latex(q0/1))
    print(f'    y_{{{i}}} = y_{{{i-2}}} - y_{{{i-1}}} * q_{{{i}}} =', latex(y0/1))
    
    if r0.degree() == 0:
        return quo(y0, r0)
    
    return xgcd(rm1, r0, ym1, y0, i+1)

x = Symbol('x')
# g(x) · f (x) ≡ w(x) mod h(x)
# input coeff mod n, g, w, h
# output f

print('Input n:')

'''
n = 7 #
h = poly(6*x**3+x**2+3, x, modulus=n) #
g = rem(poly(2*x**3+6*x**2+4*x+5, x, modulus=n), h) #
w = poly(5*x+4, x, modulus=n) #
'''
n = int(input()) # 7
print('Input h:') # 6*x**3+6*x
h = poly(input(), x, modulus=n) #
#g = poly(3*x**3+5*x**2+6*x+1, x, modulus=n) #
print('Input g:') #3*x**3+5*x**2+6*x+1 
g = rem(poly(input(), x, modulus=n), h) #
print('Input w:')# 5*x+1
w = poly(input(), x, modulus=n) #
#'''
ym2 = poly(0, x, modulus=n)
ym1 = poly(1, x, modulus=n)

sys.stdout = open('out/2_1.txt', 'w')

print(f'All coefficients are mod {n}')

print('#0\n    r_{-2} =', latex(h/1))
print('    r_{-1} =', latex(g/1))
print('    y_{-2} = 0\n    y_{-1} = 1')

#f = rem(invert(g, h)*w, h)
f = rem(xgcd(h, g, ym2, ym1, 0) * w, h)

lhs = rem(g*f, h)
rhs = w
correct = lhs == rhs
print('Check:', latex(lhs/1), '==', latex(rhs/1), 'is', correct)

if correct: print('CHECK PASSED!')

print('\nAnswer: f(x) =', latex(f/1))
print('Invert:', latex(rem(invert(g, h) * w, h)/1))

sys.stdout.close()
sys.stdout = stdout_fileno

print('File written')
