# + adição
# - subtração
# * multiplicação
# / divisão
# ** potênciação
# // divisão inteira
# % resto da divisão
# == igual

print (float( 5 + 2 ))
print (float( 5 - 2 ))
print (float( 5 * 2 ))
print (float( 5 / 2 ))
print (float( 5 ** 2 ))
print (float( 5 // 2 ))
print (float( 5 % 2 ))

# Ordem de precedência

#1°  ()
#2°  **
#3°  *  /  //  %
#4°  +  -

n = input("Fale um nome  ")

# {:20} vai aparecer em 20 caracteres
print ("Aparece aqui {:20} .".format(n) )

# {:>20} vai aparecer em 20 caracteres porém alinhado à direta
print ("Aparece aqui {:>20} .".format(n) )

# {:<20} vai aparecer em 20 caracteres porém alinhado à esquerda
print ("Aparece aqui {:<20} .".format(n) )

# {:^20} vai aparecer em 20 caracteres porém alinhado à cima
print ("Aparece aqui {:^20} .".format(n) )


# É possivel fazer a linha continuar sem quebrar usando   end=' '
print (n, end=' ') 
print (n)