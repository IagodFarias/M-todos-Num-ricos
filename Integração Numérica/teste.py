import numpy as np
import matplotlib.pyplot as plt

# Função Gaussiana
f = lambda x: np.exp(-x**2)

# Intervalo de x para o gráfico
x = np.linspace(-5, 5, 1000)

# Valores da função Gaussiana
y = f(x)

# Plot do gráfico da função Gaussiana
plt.plot(x, y, color='blue', label='Gaussiana')

# Preenchimento da área sob a curva
x_fill = np.linspace(-5, 5, 1000)
y_fill = f(x_fill)
plt.fill_between(x_fill, y_fill, 0, where=(y_fill > 0), color='lightblue', alpha=0.5, label='Área sob a curva')

# Configurações do gráfico
plt.title('Curva Gaussiana e Área Sob a Curva')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

# Cálculo da integral aproximada
from scipy import integrate
integral, _ = integrate.quad(f, -np.inf, np.inf)

# Texto com o valor da integral
text = f'Integral: {integral:.4f}'
plt.text(-4, 0.2, text, fontsize=10, ha='left')

# Exibição do gráfico
plt.show()


