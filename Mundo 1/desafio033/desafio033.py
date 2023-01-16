n1 = int(input('Qual o primeiro número? '))
n2 = int(input('Qual o segundo número? '))
n3 = int(input('Qual o terceiro número? '))
n11 = 0
n22 = 0
n33 = 0
################
if (n1 - n2) >= 1:
    n11 = n11 + 1 
else:
    n11 = n11 + 0
################
if(n1 - n3) >= 1:
    n11 = n11 + 1
else:
    n11 = n11 + 0
################
if (n2 - n1) >= 1:
    n22 = n22 + 1
else:
    n22 = n22 + 0
################
if (n2 - n3) >= 1:
    n22 = n22 + 1
else:
    n22 = n22 + 0
################
if (n3 - n2) >= 1:
    n33 = n33 +1
else:
    n33 = n33 + 0
################
if (n3 - n1) >= 1:
    n33 = n33 + 1 
else:
    n33 = n33 + 0
################
if n11 == 2:
    print('O primeiro valor foi o maior!')
elif n22 == 2:
    print('O segundo valor foi o maior!')
else:
    print('O terceiro valor foi o maior!')
################
if n11 == 0:
    print('O primeiro valor foi o menor!')
elif n22 == 0:
    print('O segundo valor foi o menor!')
else:
    print('O terceiro valor foi o menor!')