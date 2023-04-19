import numpy as np

vector = np.array(range(0,5))
print(vector)

#percorrendo vetor com for

for i in vector:
    print(i)


# Operações com vetores

c = vector + 2
d = vector - 2
e = vector * 2
f = vector / 2

print(c,d,e,f)


# alguns métodos numpy

np.zeros(2)
np.ones(2)
np.arange(4) #array([0, 1, 2, 3])
np.arange(2, 9, 2) #array([2, 4, 6, 8]) / np.arange(star, end, passo)

np.sort(vector)
