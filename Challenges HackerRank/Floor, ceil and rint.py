import numpy as np
np.set_printoptions(legacy = '1.13')

entrada = np.array(input().split())
entrada = [float(i) for i in entrada]

print(np.floor(entrada))
print(np.ceil(entrada))
print(np.rint(entrada))
