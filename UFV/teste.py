def bubble_sort(lista):
    tamanho = len(lista)
    organizado = False

    while not organizado:
        organizado = True
        for i in range(0,tamanho-1):
            if lista[i] > lista[i+1]:
                organizado = False
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista

print(bubble_sort([5,24,75,887,43]))