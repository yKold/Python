ano = int(input('Qual o ano atual? '))
totalmaior = 0
totalmenor = 0
for x in range(1, 8):
    nasc = int(input('Em que ano a {} pessoa nasceu? '.format(x)))
    idade = ano - nasc
    if idade >= 21:
        print('Essa pessoa é maior de idade!')
        totalmaior = totalmaior + 1
    else: 
        print('Essa pessoa é menor de idade!')
        totalmenor = totalmenor + 1
print('''O total de maiores de idade foi igual a : {}
E o total de menores de idade foi igual a {}'''.format(totalmaior, totalmenor))
