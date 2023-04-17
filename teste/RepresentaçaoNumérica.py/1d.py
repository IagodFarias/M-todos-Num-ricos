from math import sqrt
import numpy as np
from numpy import linalg
a = 21 
b = 30
e = 21 ** 2
g = 30 ** 2
f = g + e
z = sqrt(f)
c = [a,b]
d = linalg.norm(c)
print(f'{d}')
print(f"{z}")