n1 = int(input('Qual a primeira nota? '))
n2 = int(input('Qual a segunda nota? '))
s = ((n1 + n2) / 2)
if s < 5:
    print('Você foi reprovado! ')
elif s >= 7:
    print('Você foi aprovado!')
else:
    print('Você ficou de recuperação!')
print(s)
