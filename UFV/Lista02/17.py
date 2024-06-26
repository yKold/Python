x = int(input())
if x < 16:
    print("Não eleitor")
elif x > 18 and x < 65:
    print("Eleitor obrigatorio")
else:
    print("Eleitor facultativo")