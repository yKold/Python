teste = int(input())
for i in range(teste):
    entrada = str(input()).split()
    nome = entrada[0]
    forca = int(entrada[1])
    if forca <= 50 or nome == "Thor":
        print("Y")
    else:
        print("N")

