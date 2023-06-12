from scipy import integrate
import numpy as np

a = 1.0
b = 10000

F = lambda x: 1/(1+x**2)

I_quad = integrate.quadrature(F, a, b)

print(I_quad)