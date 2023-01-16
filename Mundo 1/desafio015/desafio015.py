km = float(input("Quantos Km o carro alugado percorreu? "))
d = float(input("Por quantos dias o carro foi alugado? "))
vkm = km * 0.15
vd = d * 60
pap = vkm + vd

print ("O valor a se pagar no carro por {:.2f} dias será de {:.2f} .".format(d, pap))