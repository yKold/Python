d = float(input('Qual a distância da viagem? '))
if d <= 200:
    print('O valor da passagem será de R${}.'.format( d * 0.50))
else:
    print('O valor da passagem será de R${}.'.format( d * 0.45))