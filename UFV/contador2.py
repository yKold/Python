def funcao(a):
    a += 4
    if a < 10:
        funcao(a)
    else:
        return print(a)

funcao(1)