n = input('Digite um nome completo: ')
nm1 = n.strip().capitalize().split()[0]
nm2 = n.strip().capitalize().split()[-1]
print(nm1, nm2)