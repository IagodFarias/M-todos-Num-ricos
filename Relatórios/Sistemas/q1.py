import numpy as np
from scipy.linalg import lu

def Gauss_Siedel(A, b, max_it):
    """
    Resolver um sistema pelo metodo de Gauss-Seidel
    :param A: Matriz dos coeficientes
    :param P: Matriz dos valores independentes.
    :param max_it(opcional): O numero de iterações maxima.
    :return: Matriz da solução.
    """
    xn = np.copy(b) * 0
    for c in range(0, max_it):
        for i in range(len(xn)):
            s = b[i].copy()  # s = posição de P
            for j in range(len(xn)):
                if i != j:
                    s -= A[i, j] * xn[j]  # Subtraimos tds A*x exceto onde no x[i]
            s /= A[i, i]  # Dividimos pelo A em questão
            xn[i] = s
    return xn

A = np.array([[1, -2, -1/2],
              [-2, 1, 1/2],
              [0, 1, 2]], dtype='float64')
y = np.array([[-4, 4, 0]], dtype='float64') #termos independentes
y = np.transpose(y)
x = np.linalg.solve(A, y)


P, L, U = lu(A)
A = np.dot(P, A)

print('solucao do sistema (inversão da matriz A): ', x)
epsilon = 1e-6
s = Gauss_Siedel(A, y, 100)
print('solucao do sistema (metodo de Gauss-Seidel): ', s)
print('solucao direta do sistema : ', x)
