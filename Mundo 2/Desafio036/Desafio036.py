vc = int(input('Qual o valor da casa?  '))
sl = int(input('Qual o salário do comprador? '))
yr = int(input('Em quantos anos ele vai pagar? '))
parcela = (vc / yr) / 12
if  parcela >= 0.30 * sl:
    print('Não foi possível executar o empréstimo!')
else:
    print('O empréstimo foi concluido com sucesso!')