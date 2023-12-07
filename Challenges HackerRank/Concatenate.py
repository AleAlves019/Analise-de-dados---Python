import numpy

r1 = list(input())
A = []
B = []

for i in range(int(r1[0])+ int(r1[2])):
    r = list(input())
    r = [int(elemento) for elemento in r if elemento != " "]
    A.append([r[0]])
    B.append([r[1]])

# Convertendo as listas em arrays
A = numpy.array(A)
B = numpy.array(B)

print(numpy.concatenate((A, B), axis = 1))