

import numpy as np 
import matplotlib.pyplot as plt

class raizes:

    def __init__(self, f, n=0, Emax=0.001, maxit=10):
        """
        Encontra a raiz de um polinomio.
        :param n: Palpite inicial.
        :param f: Função a ser usada.
        :param f_linha: Derivada da função a ser usada.
        :param sigma: Função atualizadora de x para o metodo do ponto fixo.
        :param Emax: Erro maximo.
        :param maxit: Numero maximo de iterações.
        :param a, b: Limites inferior e superior de um intervalo no qual deverá conter a raiz.
        :param x0, x1: Chutes iniciais para o metodo da secante.
        :param d: Valor de pertubação da raiz, caso não especificado será 0.0001.
        :param x: Raiz da função.
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
        convergencia = [] # lista para armazenar os valores de convergência da raiz
        erros = [] # lista para armazenar os valores de erro

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

            convergencia.append(self.x) # adiciona o valor atual de self.x na lista de convergência
            erros.append(self.erro) # adiciona o valor atual de erro na lista de erros

            if self.erro <= self.Emax or cont >= self.maxit:
                break

        plt.plot(convergencia) # cria o gráfico de convergência da raiz
        plt.title("Convergência da raiz")
        plt.xlabel("Iteração")
        plt.ylabel("Raiz")
        plt.show()

        plt.plot(erros) # cria o gráfico de convergência do erro
        plt.title("Convergência do erro")
        plt.xlabel("Iteração")
        plt.ylabel("Erro")
        plt.show()





    def posicao_falsa(self, a, b):

        xrold = 0
        cont = 0
        erros = [] # lista para armazenar os erros em cada iteração
        lista_raizes = [] # lista para armazenar as raízes em cada iteração

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

            erros.append(self.erro) # adiciona o erro à lista
            lista_raizes.append(self.x) # adiciona a raiz à lista

            if self.erro <= self.Emax or cont >= self.maxit:
                break

    # plotar os gráficos de convergência de erro e raiz
        plt.figure(figsize=(8, 6))
        plt.plot(lista_raizes, 'g-', label='Raiz')
        plt.legend()
        plt.xlabel('Iterações')
        plt.ylabel('Valor')
        plt.title('Convergência da Posição Falsa')
        plt.show()

r = raizes(lambda x: x**2 - 5)
#r.bissecao(2, 3)
#print(f"Raiz encontrada: {r.x}")

r.posicao_falsa(2, 3)
print(f"Raiz encontrada: {r.x}")




