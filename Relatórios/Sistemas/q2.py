import math
from sympy import symbols, exp, diff, lambdify

def v(t):
    return 1 - (1 + t + (t**2)/2) * math.exp(-t) - 0.67

def dv(t):
    t_sym = symbols('t')
    v_sym = 1 - (1 + t_sym + (t_sym**2)/2) * exp(-t_sym)
    dv_sym = diff(v_sym, t_sym)
    dv_fn = lambdify(t_sym, dv_sym, "numpy")
    return dv_fn(t)

def Método_Newton():
    x0 = 1  # Valor inicial
    epsilon = 0.000001  # Precisão desejada
    max_iterations = 1000  # Número máximo de iterações
    
    x = x0
    iteration = 0
    while abs(v(x)) > epsilon and iteration < max_iterations:
        if abs(dv(x)) < epsilon:
            # Evitar divisão por zero, atualizando o valor inicial
            x0 += epsilon
        x = x - v(x) / dv(x)
        iteration += 1
    
    if abs(v(x)) <= epsilon:
        return x  # Encontrou uma solução aproximada
    
    return None  # Não encontrou uma solução dentro do número máximo de iterações

# Chama o método para resolver a equação
solution = Método_Newton()

if solution is not None:
    print("A solução aproximada é:", solution)
else:
    print("Não foi possível encontrar uma solução.")
