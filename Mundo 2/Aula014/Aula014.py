# c = 1
# while c < 10:
    # print(c)
    # c = c + 1
# print('fim')

# n = 1
# while n != 0:
    # n = int(input('valor: '))
# print('Fim')

n = 1
par = 0
impar = 0 
while n != 0:
    n = int(input('valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} pares e {} impares'.format(par, impar))
print('Fim')