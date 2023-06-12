import numpy as np

a = 0
b = np.pi
n = 701
h = (b - a) / (n - 1)
x = np.linspace(a, b, n)

F = np.exp(np.sin(x))

I_simp = (h/3) * (F[0] + 4*sum(F[1:n-1:2]) \
            + 2*sum(F[2:n-2:2]) + F[n-1])

print(I_simp)