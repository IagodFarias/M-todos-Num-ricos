import numpy as np

a = 0
b = np.pi
n = 1000

h = (b - a) / n

x = np.linspace(a, b, n+1)
f = np.exp(np.sin(x))

integral = (h/2) * (f[0] + 2 * np.sum(f[1:n]) + f[n])

print(integral)
