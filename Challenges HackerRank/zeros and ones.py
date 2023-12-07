import numpy as np

entrada = list(input())
entrada = [int(elemento) for elemento in entrada if elemento != " "]

print(np.zeros((entrada), dtype = np.int))
print(np.ones((entrada), dtype = np.int))