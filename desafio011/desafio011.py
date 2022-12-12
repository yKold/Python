l = int(input('Qual a largura da parede? '))
a = int(input('Qual a altura da parede? '))
area = a * l
print('A área da sua parede é igual a {} metros quadrados e para pinta-lá utilizando uma lata de tinta na qual cada litro pinta 2 metros quadrados, serão utilizados {} litros de tinta.'.format(area, area / 2))