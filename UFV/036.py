import math
Valor = input().split()
A = float(Valor[0])
B = float(Valor[1])
C = float(Valor[2])


DELTA = (B**2) - (4*A*C)


if A == 0 or (DELTA ** (1/2)).imag !=0:
    print("Impossivel calcular")
else:
    BHASKARA1 = (-B + DELTA ** (1/2))/ (2*A)
    BHASKARA2 = (-B - DELTA ** (1/2))/ (2*A)
    print("R1 = {:.5f}\nR2 = {:.5f}".format(BHASKARA1, BHASKARA2))




