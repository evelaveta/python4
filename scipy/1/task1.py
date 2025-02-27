from sympy import *
from sympy.abc import *
init_printing(use_unicode=True)

lmbd = var('lambda')
rho, mu = symbols('rho mu')
A = -1/rho * eye(3)
A = A.col_insert(3, zeros(3, 3))
A = A.col_insert(0, zeros(3, 3))
A = A.row_insert(3, zeros(6, 9))

B = diag(-(lmbd + 2*mu), -mu, -mu)
B = B.col_insert(3, zeros(3, 6))
B = B.row_insert(0, zeros(3, 9))
B = B.row_insert(6, zeros(3, 9))

C = Matrix([-lmbd, 0 , -lmbd])
C = C.col_insert(1, zeros(3, 8))
C = C.row_insert(0, zeros(6, 9))

M = A + B + C
pprint(M.eigenvals())
pprint(M)
