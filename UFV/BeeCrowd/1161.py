def fatorial(nmr):
    res = 1
    for i in range(nmr):
        res *= i+1
    return res

while True:
    try:
        G = input().split()
        
        M = int(G[0])
        N = int(G[1])

        if 20 >= M >= 0 or 20 >= N >= 0:
            if M == 0:
                M = 1
            elif N == 0:
                N = 1
            soma = fatorial(M) + fatorial(N)
            print(soma)

        
    except EOFError:
        break