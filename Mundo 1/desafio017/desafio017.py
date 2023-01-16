import math
co = float(input('Qual o cateto oposto? '))
ca = float(input('Qual o cateto adjascente? '))
h = math.hypot(co, ca)
print('A hipotenusa é igual a {:.2f}'.format(h))