while True:
    ano = int(input('Qual o ano de seu nascimento? '))
    ano_atual = int(input('Qual o ano atual? '))
    idade = ano_atual - ano
    print('De acordo com a lei de alistamento obrigatório: ')
    if idade < 18:
        print('Ainda faltam {} anos para você se alistar!'.format( 18 - idade ))
    elif idade == 18:
        print('Você já está na idade de fazer o alistamento, procure saber onde deverá ser feito em sua região!')
    else:
        print('Já se passaram {} anos da idade obrigatória para o alistamento, procure como realizar o exame caso não tenha feito ainda, desde já muito obrigado!'.format( idade - 18 ))


