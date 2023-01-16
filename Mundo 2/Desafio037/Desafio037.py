while True:
    n = int(input('Escolha um número inteiro: '))
    base = int(input('Digite para qual base deseja converter seu número: \n [1] Binária \n [2] Octal \n [3] Hexadecimal\n \n'))
    if base == 1:
        print('O seu novo número é {}.'.format(bin(n)))
        break  
    elif base == 2:
        print('O seu novo número é {}.'.format(oct(n)))
        break
    elif base == 3:
        print('O seu novo número é {}.'.format(hex(n)))
        break
    else:
        print('O valor digitado não é compatível com as opções, por favor, digite novamente!')
