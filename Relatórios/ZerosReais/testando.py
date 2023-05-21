
from math import log
import numpy as np
from scipy.linalg import lu_factor, lu_solve
from scipy.interpolate import interp1d

# =============================================================================
# Projeto MÃ©todos NumÃ©ricos: Calculadora de mÃ©todos
# =============================================================================


class raizes:

    def __init__(self, f, n=0, Emax=0.001, maxit=10):
        """
        Encontra a raiz de um polinomio.
        :param n: Palpite inicial.
        :param f: FunÃ§Ã£o a ser usada.
        :param f_linha: Derivada da funÃ§Ã£o a ser usada.
        :param sigma: FunÃ§Ã£o atualizadora de x para o metodo do ponto fixo.
        :param Emax: Erro maximo.
        :param maxit: Numero maximo de iteraÃ§Ãµes.
        :param a, b: Limites inferior e superior de um intervalo no qual deverÃ¡ conter a raiz.
        :param x0, x1: Chutes iniciais para o metodo da secante.
        :param d: Valor de pertubaÃ§Ã£o da raiz, caso nÃ£o especificado serÃ¡ 0.0001.
        :param x: Raiz da funÃ§Ã£o.
        """
        self.f = f
        self.Emax = Emax
        self.maxit = maxit
        self.n = n
        self.x = None
        self.erro = None
        self.iter = None

    def bissecao(self, a, b):

        xrold = 0
        cont = 0

        while True:
            self.x = (a + b) / 2
            cont += 1

            if self.f(a) * self.f(self.x) < 0:
                b = self.x
                self.erro = abs(self.x - xrold)
            elif self.f(b) * self.f(self.x) < 0:
                a = self.x
                self.erro = abs(self.x - xrold)
            else:
                self.erro = 0

            xrold = self.x
            self.iter = cont

            if self.erro <= self.Emax or cont >= self.maxit:
                break

def f(x):
    y = x * np.log(x) - 1
    return y

z = raizes(f)
z.bissecao(1, 2)
print(z.x)
print(z.iter)