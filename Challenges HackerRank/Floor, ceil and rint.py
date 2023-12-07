import numpy as np
np.set_printoptions(legacy = '1.13')

entrada = np.array(input().split())
entrada = [float(i) for i in entrada]

print(np.floor(entrada))# Arredonda para o menor numero inteiro
print(np.ceil(entrada))# arrendonda para o maior numero inteiro
print(np.rint(entrada)) # arrendonda para o inteiro mais proximo
