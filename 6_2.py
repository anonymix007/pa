from sympy import *

# input m, n, H, u1, u2
# output v1, v2 ( = encoded u1, u2)

#'''
m = 7 #
n = 3 #
H = Matrix([[0,1,1,1,0,0,0],[0,1,0,1,0,1,0],[1,0,1,0,0,1,1]]) #
u1 = Matrix([1,1,0,0]) #
u2 = Matrix([1,1,1,0]) #
'''

#'''

RREF, pivot = H.rref(iszerofunc=lambda x: x % 2 == 0)
#print(f'Code is ({m}, {n}), so {m} bits in encoded words, {n} bits in to-be-coded words')
RREF%=2
print('Row reduced:')
pprint(RREF)
#print(pivot)
assert(pivot == tuple(range(n)))

G = Matrix(RREF)
for _ in range(n):
    G.col_del(0)
#pprint(G)
#print(G.shape)

I44 = eye(m-n)
#pprint(I44)
for i in range(m-n):
    G = G.row_insert(n+i, I44.row(i))

print('Generating matrix:')
pprint(G)

pprint(u1.T)
pprint(u2.T)

v1 = (G * u1) % 2
v2 = (G * u2) % 2
print('\nAnswer: \nEncoded u_{1}^{T} is:')
pprint(v1.T)
print('Encoded u_{2}^{T} is:')
pprint(v2.T)
