
import numpy as np 
from math import sqrt


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

        xrold = 0 # é usada para armazenar o valor anterior de self.x
        cont = 0 # quantidade de interações

        while True:
            self.x = (a + b) / 2
            cont += 1

            if self.f(a) * self.f(self.x) < 0:      #A condição if é verificada para determinar se a raiz está à
                                                    #esquerda ou à direita de self.x. Se o produto das funções self.f(a) e self.f(self.x) for negativo, 
                                                    # a raiz está à esquerda e, portanto, b é atualizado como self.x. Caso contrário, 
                                                    # se o produto das funções self.f(b) e self.f(self.x) 
                                                    #for negativo, a raiz está à direita e a é atualizado como self.x. 
                                                    # Se o produto for zero, significa que self.x é a própria raiz.
                b = self.x
                self.erro = abs(self.x - xrold)
            elif self.f(b) * self.f(self.x) < 0:
                a = self.x
                self.erro = abs(self.x - xrold)
            else:
                self.erro = 0

            xrold = self.x
            self.iter = cont #atualização do número de interções

            if self.erro <= self.Emax or cont >= self.maxit:   #Critério de parada
                break

    def posicao_falsa(self, a, b):

        xrold = 0
        cont = 0

        while True:
            self.x = ((a * self.f(b)) - (b * self.f(a))) / (self.f(b) - self.f(a))
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
    return x - sqrt(5)

raiz = raizes(f)
#a, b = 0, 5
x = raiz.bissecao(0, 5)
print(x)