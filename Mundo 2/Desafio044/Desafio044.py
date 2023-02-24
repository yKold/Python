p = float(input('Qual o preço do produto? '))
print('''As opções são
1 = à vista no dinheiro ou cheque '
2 = à vista no cartão
3 = 2x no cartão
4 = 3x ou mais no cartão ''')
c = int(input('Qual a condição de pagamento do produto? '))

if c == 1:
    print('O valor será de : {}'.format(p - (10/100 * p)))
elif c == 2:
    print('O valor será de : {}'.format(p - (5 / 100 * p)))
elif c == 3:
    parcela = p / 2
    print('O valor será normal de {} por parcela! '.format(parcela))
else: 
    parcelas = int(input('Quantas parcelas? '))
    juros = p + (p * 20 / 100)
    p = juros
    parcela = p / parcelas
    print('O valor será de {} por parcela! '.format(parcela))