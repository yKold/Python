# lista = ["batata", "maca"]
# for x in lista:
#     print(x, end="") // ao final da linha ele continua

# npcs = [
#     {"name": "monstro 1", "level": 1},
#     {"name": "monstro 2", "level": 2},
#     {"name": "monstro 3", "level": 3},
#     {"name": "monstro 4", "level": 4}
# ]

# for x in npcs:
#     print(x["name"]) // procura o "name"


x = 0
y = 100
tam = y - x
val = []
teste = []


for i in range(tam-1):
    val.append(x + (i+1))
for i in val:
    o = i
    i = str(i)
    if o > 9 and o <= 99:
        a = i[:1]
        b = i[1:2]
        if a != b :
            print(i)
            teste.append(i)
    
        
print(teste)

