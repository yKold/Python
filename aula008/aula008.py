from math import sqrt, floor, ceil 
import random
import emoji

n = int(input("Me diga um número: "))
rz = int(sqrt(n))
print('A raiz quadrada de {} é igual a {} .'.format(n, rz))

#  ceil = arredonda para cima
#  floor = arredonda para baixo


num = random.randint(1, 20)
print(num)

print(emoji.emojize('Hoje o dia está :rosto_fervendo_de_calor:', language='pt'))