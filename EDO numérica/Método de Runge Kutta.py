import numpy as np
import matplotlib.pyplot as plt

def runge_kutta_4(f, x0, y0, x1, n):
    vx = np.linspace(x0,x1,n+1)
    vy = np.zeros(n+1)
    vy[0] = y0
    h = (x1-x0)/n
    
    for i in range(1,n+1):
        k1 = h * f(vx[i-1], vy[i-1])
        k2 = h * f(vx[i-1] + 0.5*h, vy[i-1] + 0.5*k1)
        k3 = h * f(vx[i-1] + 0.5*h, vy[i-1] + 0.5*k2)
        k4 = h * f(vx[i-1] + h, vy[i-1] + k3)
        vy[i] = vy[i-1] + (k1 + 2*k2 + 2*k3 + k4) / 6
        print(f"x = {vx[i]}, y = {vy[i]}")
    
    return vx, vy

# f(x,y) significa dy/dx na visualização de uma EDO
def f(x, y):
    return -50 * y + 5000

vx, vy = runge_kutta_4(f, 0, 0, 0.01, 1000)
plt.plot(vx, vy)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
