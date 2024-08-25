while True:
    try:
        x = int(input())
        esquerdo = []
        direito = []
        pares = 0
        for i in range(x):
            entrada = input().split()
            nmr = int(entrada[0])
            pe = entrada[1]
            if pe == "D":
                direito.append(nmr)
            elif pe == "E":
                esquerdo.append(nmr)
        for i in esquerdo:
            for j in direito:
                if i == j:
                    pares += 1
                    direito.remove(j)
                
        print(pares)
    except EOFError:
        break