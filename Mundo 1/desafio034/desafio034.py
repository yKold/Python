s = float(input('Qual o valor do seu salário? '))
if s > 1250.00:
    print('Seu novo salário será de {}.'.format((s * 0.10) + s))
else:
    print('Seu novo salário será de {}.'.format((s * 0.15) + s))
