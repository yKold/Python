teste = list()
teste.append("Gabriel")
teste.append(17)

galera = list()
galera.append(teste[:])

teste[0] = "joao"
teste[1] = 13

galera.append(teste[:])

print(galera)

batata = [["alface", 13], ["cenoura", 22]]
print(batata[0][1])