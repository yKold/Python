import random
n1 = str(input('Qual o nome do primeiro aluno? '))
n2 = str(input('Qual o nome do segundo aluno? '))
n3 = str(input('Qual o nome do terceiro aluno? '))
n4 = str(input('Qual o nome do quarto aluno? '))
l = n1, n2, n3, n4
r = random.sample(l, k=4)
print('A ordem de apresentação será: {}'.format(r))
