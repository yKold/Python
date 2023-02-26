c = str(input('Digite uma frase: '))
c = c.upper().replace(' ', '')
i = c[::-1]
#print(i)
if i == c:
    print('Esta frase é um palindromo.')
else:
    print('Esta frase não é um palindromo')