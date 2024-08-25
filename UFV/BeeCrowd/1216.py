soma = 0
contador = 0
while True:
    try:
        nome = str(input())
        distancia = int(input())
        soma += distancia
        contador+=1
    except EOFError:
        break
print(f"{(soma/contador):.1f}")