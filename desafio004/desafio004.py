esc = input('Digite alguma coisa ')

print ("A sua coisa tem um tipo {}".format(type(esc)))
print ("Ele é numérico? {}".format(esc.isnumeric()))
print ("Ele é alfabético? {}".format(esc.isalpha()))
print ("Ele é alfa-numérico? {}".format(esc.isalnum()))
print ("Ele é um número decimal? {}".format(esc.isdecimal()))
print ("Ele está em minúsculo? {}".format(esc.islower()))