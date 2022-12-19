v = float(input('Qual a velocidade do carro? '))
if v<= 80:
    print('Você não foi multado!')
else:
    m = v - 80
    print('Sua multa foi de R${}'.format( 7 * m))