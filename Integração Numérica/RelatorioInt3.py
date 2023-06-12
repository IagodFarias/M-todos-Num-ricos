from scipy import integrate
import numpy as np

a = 0
b = np.pi

f = lambda x: np.exp(np.sin(x))

I_quad = integrate.quadrature(f, a, b)

print(I_quad)
