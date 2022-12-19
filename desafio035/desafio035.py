r1 = int(input('Qual o valor da primeira reta?'))
r2 = int(input('Qual o valor da segunda reta?'))
r3 = int(input('Qual o valor da terceira reta?'))
n = 0

if (r1 + r2) > r3:
    n = n + 1
else:
    n = n + 0
if (r1 + r3) > r2:
    n = n + 1
else:
    n = n + 0
if (r2 + r3) > r1:
    n = n + 1
else:
    n = n + 0
if n == 3:
    print('É possível criar um triângulo!')
else:
    print('Não é possível criar um triângulo!')