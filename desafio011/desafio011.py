l = float(input('Qual a largura da parede? '))
a = float(input('Qual a altura da parede? '))
area = a * l
print('A área da sua parede é igual a {} metros quadrados e para pinta-lá utilizando uma lata de tinta na qual cada litro pinta 2 metros quadrados, serão utilizados {:.2f} litros de tinta.'.format(area, area / 2))