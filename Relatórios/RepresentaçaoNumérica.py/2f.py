

import numpy as np
D = np.matrix(np.arange(20,0,-2))
print(D)
Dt = np.transpose(D)
multg = Dt*D
print("\n", multg)
