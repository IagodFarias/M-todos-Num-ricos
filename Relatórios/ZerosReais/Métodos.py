
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

    def ponto_fixo(self, sigma):

        cont = 0
        xrold = 0
        self.x = self.f(self.n)

        while True:
            cont += 1
            self.iter = cont
            if abs(self.x - xrold) < self.Emax or cont >= self.maxit:
                self.erro = abs(self.x - xrold)
                break
            xrold = self.x
            self.x = sigma(self.x)

    def secante(self, x0, x1):

        cont = 0
        xrold1 = x1
        xrold2 = x0

        while True:
            self.x = xrold1 - (self.f(xrold1) * (xrold2 - xrold1)) / (self.f(xrold2) - self.f(xrold1))
            cont += 1

            self.erro = abs((self.x - xrold1) / self.x)

            xrold2 = xrold1
            xrold1 = self.x
            self.iter = cont

            if self.erro <= self.Emax or cont >= self.maxit:
                break

    def secante_mod(self, d=0.001):

        cont = 0
        xrold = self.n

        while True:
            self.x = xrold - (d * xrold * self.f(xrold)) / (self.f(xrold + d * xrold) - self.f(xrold))
            cont += 1

            self.erro = abs((self.x - xrold) / self.x)

            xrold = self.x
            self.iter = cont

            if self.erro <= self.Emax or cont >= self.maxit:
                break

    def Newton_Raphson(self, f_linha):
        contador = 0
        self.x = [self.n]  # x(n), sendo inicialmente nosso palpite
        self.iter = contador
        while True:
            contador += 1
            # a cada iteraÃ§Ã£o vamos adicionar um novo valor de x Ã  lista
            # x[-1] Ã© o ultimo elemento de uma lista
            if f_linha(self.x[-1]) == 0:
                print(f'NÃ£o foi possivel encontrar a raiz pois f_linha(x) = 0 \nEscolher outro palpite')
                return 0
            self.x.append(self.x[-1] - self.f(self.x[-1]) / f_linha(self.x[-1]))
            # x(n+1) pela formula de Newton-Raphson
            self.erro = abs(self.x[-1] - self.x[-2])  # erro absoluto
            if self.erro < self.Emax:
                break
            if self.iter > self.maxit:
                break
        self.x = self.x[-1]


class interpol:

    def __init__(self, x, y, po, pf):
        """
        Resolve problemas de interpolaÃ§Ã£o.
        :param x: Vetor com os valores de X.
        :param y: Vetor com os valores de Y.
        :param po: O valor inicial de X onde se pretende calcular a aproximaÃ§Ã£o.
        :param pf: O valor final de X onde se pretende calcular a aproximaÃ§Ã£o.
        :param tipo: O tipo de spline a ser utilizado, caso nÃ£o especificado serÃ¡ spline cubico.
        :param grau: O grau do polinomio MMQ gerado, caso nÃ£o especificado serÃ¡ grau 1.
        :param resultado: Dicionario com os valores entre os ponto pedidos e suas respectivas aproximaÃ§Ãµes de F(x).
        """
        self.x = x
        self.y = y
        self.po = po
        self.pf = pf
        self.resultado = {None}

    def Newton(self):
        tam = len(self.x)
        res = np.array([], dtype='float32')
        pontos = np.linspace(self.po, self.pf, 100)  # Intervalo a ser calculado
        for p in pontos:
            FDD = np.ones(tam ** 2).reshape(
                (tam, tam)) * -1  # Tabela de diferenÃ§as divididas(comeÃ§a em -1 para visualizaÃ§Ã£o)
            for i in range(tam):
                FDD[i][0] = self.y[i]  # Primeira coluna
            for i in range(1, tam):
                for j in range(tam - i):  # Demais colunas
                    FDD[j][i] = (FDD[j + 1][i - 1] - FDD[j][i - 1]) / (
                            self.x[j + i] - self.x[j])  # Faz todas as colunas antes de iterar a linha
            x_termo = 1  # Auxiliar para a multiplicaÃ§Ã£os pelos termos de X
            pol = FDD[0][0]  # Polinomio de Newton
            for ordem in range(1, tam):
                x_termo = x_termo * (p - self.x[ordem - 1])
                pol += FDD[0][ordem] * x_termo  # Operador(primeiro termo de cada coluna)*multiplicaÃ§Ã£o dos x
            res = np.append(res, pol)
        self.resultado = {"X": pontos,
                          "Y": res}

    def Lagrange(self):
        res = np.array([], dtype='float32')
        r = 0
        tam = len(self.x)
        pontos = np.linspace(self.po, self.pf, 100)  # Intervalo a ser calculado
        for ponto in pontos:
            for i in range(0, tam):  # Cada ordem de y(i)L(i)
                produtorio = 1  # L(i)
                for j in range(0, tam):
                    if j != i:
                        produtorio *= (ponto - self.x[j]) / (self.x[i] - self.x[j])
                r += produtorio * self.y[i]
            res = np.append(res, r)
            r = 0
        self.resultado = {"X": pontos,
                          "Y": res}

    def Spline(self, tipo=3):
        if tipo == 1:
            s = interp1d(self.x, self.y, kind='linear')
            pontos = np.linspace(self.po, self.pf, 100)  # Intervalo a ser calculado
            res = np.array([s(i) for i in pontos])
            self.resultado = {"X": pontos,
                              "Y": res}
        elif tipo == 2:
            s = interp1d(self.x, self.y, kind='quadratic')
            pontos = np.linspace(self.po, self.pf, 100)  # Intervalo a ser calculado
            res = np.array([s(i) for i in pontos])
            self.resultado = {"X": pontos,
                              "Y": res}
        else:
            s = interp1d(self.x, self.y, kind='cubic')
            pontos = np.linspace(self.po, self.pf, 100)  # Intervalo a ser calculado
            res = np.array([s(i) for i in pontos])
            self.resultado = {"X": pontos,
                              "Y": res}

    def MMQ(self, grau=1):

        def mmq(x, th, grau):  # Devolve a soma dos termos do polinomio
            aux = grau
            soma = 0
            for c in range(0, grau):
                soma += th[c] * (x ** aux)
                aux -= 1
            soma += th[-1]
            return soma

        M_x = np.ones(len(self.x) * (grau + 1)).reshape(len(self.x), grau + 1)  # Cria a matrix a ser usada
        aux = grau
        for c in range(0, grau):
            for i in range(0, len(self.x)):
                M_x[i][c] = self.x[i] ** aux
            aux -= 1
        th = np.linalg.inv(M_x.transpose().dot(M_x)).dot(M_x.transpose().dot(self.y))  # Aplica a formula do MMQ
        pontos = np.linspace(self.po, self.pf, 100)  # Intervalo a ser calculado
        res = np.array([mmq(i, th, grau) for i in pontos])
        self.resultado = {"X": pontos,
                          "Y": res}


class Sistemas_Lineares():
    def __init__(self, A, P, max_it=10):
        """
        Resolve problemas de sistemas lineares do tipo Ax=P.
        :param A: Matriz com os coeficientes de x.
        :param P: Matriz com os valores independentes.
        :param max_it: Numero maximo de iteraÃ§Ãµes.
        :param resultado: Vetor com as soluÃ§Ãµes.
        """
        self.A = A
        self.P = P
        self.max_it = max_it
        self.resultado = None

    def LU(self):
        lu, piv = lu_factor(self.A)
        self.resultado = lu_solve((lu, piv), self.P)

    def Gauss_Siedel(self):
        self.resultado = np.copy(self.P) * 0
        for c in range(0, self.max_it):  # Repete quantas vezes forem passadas
            for i in range(len(self.resultado)):
                s = self.P[i].copy()  # s = posiÃ§Ã£o de P
                for j in range(len(self.resultado)):
                    if i != j:
                        s -= self.A[i, j] * self.resultado[j]  # Subtraimos tds A*x exceto onde no x[i]
                s /= self.A[i, i]  # Dividimos pelo A em questÃ£o
                self.resultado[i] = s  # Atualizamos vetor resultado


class EDO():
    def __init__(self, f_linha, xi, fi, h=0.1):
        """
        Encontra a aproximaÃ§Ã£o da EDO por um metodo numerico.
        :param f_linha: Derivada isolada da funÃ§Ã£o.
        :param xi: PosiÃ§Ã£o da condiÃ§Ã£o conhecida.
        :param fi: CondiÃ§Ã£o conhecida.
        :param h: Valor do passo, caso nÃ£o especificado serÃ¡ 0.1.
        :param x_anterior: Variavel auxiliar para aplicaÃ§Ã£o do metodo.
        :param y_anterior: Valor passado da aproximaÃ§Ã£o da soluÃ§Ã£o da EDO no ponto t.
        :param y_novo: Valor da aproximaÃ§Ã£o da soluÃ§Ã£o da EDO no ponto t.
        :param t: PosiÃ§Ã£o do valor no qual deseja ser encontrado.
        """
        self.f_linha = f_linha
        self.xi = xi
        self.fi = fi
        self.h = h
        self.x_anterior = None
        self.y_anterior = None
        self.y_novo = None

    def Euler(self, t):
        self.t = t
        if self.xi == self.t:  # Retorna valor conhecido caso busquemos sua posiÃ§Ã£o.
            self.y_novo = self.fi

        n = int((self.t - self.xi) / self.h)
        self.y_anterior = self.fi
        self.x_anterior = self.xi
        for p in range(0, n):  # Aplica a formula n vezes.
            self.y_novo = self.y_anterior + self.h * self.f_linha(self.x_anterior, self.y_anterior)
            self.x_anterior += self.h  # Atualiza o valor de x.
            self.y_anterior = self.y_novo  # Atualiza o valor de y.

    def Heun(self, t):
        self.t = t
        if self.xi == self.t:  # Retorna valor conhecido caso busquemos sua posiÃ§Ã£o.
            self.y_novo = self.fi

        n = int((self.t - self.xi) / self.h)
        for p in range(0, n):  # Aplica a formula n vezes.
            if p == 0:
                self.y_anterior = self.fi
                self.x_anterior = self.xi
            self.y_novo = self.y_anterior + (self.h / 2) * (self.f_linha(self.x_anterior, self.y_anterior) +
                                                            self.f_linha(self.x_anterior + self.h,
                                                                         self.y_anterior + self.h * self.f_linha(
                                                                             self.x_anterior,
                                                                             self.y_anterior)))
            self.x_anterior += self.h  # Atualiza o valor de x.
            self.y_anterior = self.y_novo  # Atualiza o valor de y.

    def Runge_Kutta_4(self, t):
        self.t = t
        if self.xi == self.t:  # Retorna valor conhecido caso busquemos sua posiÃ§Ã£o.
            self.y_novo = self.fi

        n = int((self.t - self.xi) / self.h)
        for p in range(0, n):  # Aplica a formula n vezes.
            if p == 0:
                self.y_anterior = self.fi
                self.x_anterior = self.xi
            k1 = self.f_linha(self.x_anterior, self.y_anterior)
            k2 = self.f_linha(self.x_anterior + 0.5 * self.h, self.y_anterior + k1 * 0.5 * self.h)
            k3 = self.f_linha(self.x_anterior + 0.5 * self.h, self.y_anterior + k2 * 0.5 * self.h)
            k4 = self.f_linha(self.x_anterior + self.h, self.y_anterior + k3 * self.h)
            self.y_novo = self.y_anterior + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4) * self.h
            self.x_anterior += self.h  # Atualiza o valor de x.
            self.y_anterior = self.y_novo  # Atualiza o valor de y.


class Integral():
    def __init__(self, f, a, b, n=1):
        """
        Encontra a aproximaÃ§Ã£o da integral por um metodo numerico.
        :param f: FunÃ§Ã£o a ser integrada.
        :param a: Limite de integraÃ§Ã£o inferior.
        :param b: Limite de integraÃ§Ã£o superior.
        :param n: Quantidade de subdiviÃ§Ãµes do metodo, serÃ¡ 1 caso nÃ£o especificado.
        :param resultado: Valor da aproximaÃ§Ã£o.
        """
        self.f = f
        self.a = a
        self.b = b
        self.n = n
        self.resultado = None

    def Trapezio(self):
        h = (self.b - self.a) / self.n
        x = np.arange(self.a, self.b + h, h)
        y = np.array([self.f(i) for i in x])
        soma = y.sum()
        self.resultado = (h / 2) * ((2 * soma) - y[0] - y[-1])

    def Simpson(self):
        h = (self.b - self.a) / (2 * self.n)
        x = np.arange(self.a, self.b + h, h)
        y = np.array([self.f(i) for i in x])
        for i in range(len(y)-1):
            if i == 0:
                par = 0
                impar = 0
            elif i % 2 == 0:
                par += y[i]
            else:
                impar += y[i]
        self.resultado = (h / 3) * (y[0] + y[-1] + 2 * par + 4 * impar)