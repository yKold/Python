n = int(input("Digite o número: "))
for c in range(2, n):
    if (n % c) == 0:
        print('Não é primo.')
    else:
        print('Número é primo.')