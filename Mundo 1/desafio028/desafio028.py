import random
r = random.randint(0, 5)
print(r)
n = int(input('Qual número de 0 a 5 você acha que caiu? '))
if n == r:
    print('Parabéns você adivinhou o número')
else:
    print('Você infelizmente errou')