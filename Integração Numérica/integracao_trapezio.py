import numpy as np

a = 0
b = 1.2
n = 70001
h = (b - a) / (n - 1)
x = np.linspace(a, b, n)
f = np.cos(x)
g = np.exp(x)

F = f*g

I_trap = (h/2)*(F[0] + \
     2 * sum(F[1:n-1]) + \
        F[n-1])

err_trap = 1.6487744273474478 - I_trap

print(I_trap)
print(err_trap)
