import numpy as np
import sympy as sp
from math import cos, sin
x1, x2 = sp.symbols('x1 x2')

def jacobiana(F, Xj, xj):
    a = np.arange(0, len(F), 1)
    v = Xj
    fj = np.ones(len(a))
    for k in a:
        v[k] = (Xj[k], xj[k])
    Jac = np.zeros((len(F), len(Xj)))
    for i in a:
        fj[i] = -F[i].subs(v)
    for j in a:
        dfx = sp.diff(F[i], Xj[j])
        Jac[i][j] = dfx.subs(v)
    return Jac, fj


f1 = 5 * x1**2 - x2**2
f2 = x1 - 0.25*(sp.sin(x1) - sp.cos(x2))
F = [f1, f2]
X = [x1, x2]
xs = [0.5, 0.5]
epsilon = 1e-6
norma_inf = 1

while norma_inf > epsilon:
    a = np.arange(0, len(F), 1)
    x0 = xs
    Jac, fs = jacobiana(F, X, x0)
    X = [x1, x2]
    sJ = np.linalg.inv(Jac)
    for i in a:
        fs[i] = fs[i]
    s = np.matmul(sJ, np.transpose(fs))
    norma_inf = max(abs(s))
    xs = x0 + s
print('A solucao do sistema e: ',xs)
