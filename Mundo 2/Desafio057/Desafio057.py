s = str(input('Qual o seu sexo: ')).strip().upper()
while s not in 'MmFf':
    s = str(input('Incorreto, informe novamente: ')).upper().strip()
print('ok')
