import numpy as np
from scipy.linalg import lu

def Gauss_Seidel(A, b, max_it):
    xn = np.zeros_like(b)
    for c in range(max_it):
        for i in range(len(xn)):
            s = b[i].copy()  # s = posição de P
            for j in range(len(xn)):
                if i != j:
                    s -= A[i, j] * xn[j]  # Subtraímos todos os A*x, exceto onde não há x[i]
            s /= A[i, i]  # Dividimos pelo A em questão
            xn[i] = s
    return xn

A = np.array([[1, -2, -1/2],
              [-2, 1, 1/2],
              [0, 1, 2]], dtype='float64')
b = np.array([-4, 4, 0], dtype='float64')

P, L, U = lu(A)
A = np.dot(P, A)  # Reorganiza a matriz A de acordo com a matriz de permutação P

x_direct = np.linalg.solve(A, b)  # Solução direta usando a função solve

epsilon = 1e-6  # Critério de convergência
max_iter = 100  # Número máximo de iterações

x_iterative = Gauss_Seidel(A, b, max_iter)  # Solução iterativa usando o método de Gauss-Seidel

print('Solução do sistema (método direto):', x_direct)
print('Solução do sistema (método iterativo):', x_iterative)
