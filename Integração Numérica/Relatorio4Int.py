from scipy import integrate
import numpy as np

f = lambda x: np.exp(-x**2)

integral, _ = integrate.quad(f, -np.inf, np.inf)

print(integral)
