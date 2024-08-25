# x = [0, 1]
# y = int(input())
# while y > 60 or y < 0:
#     y = int(input())
# for i in range(y):
#     valor = x[i+1] + x[i]
#     x.append(valor)
# print(f"Fib ({y}) = {x[y]}")





while True:
    try:
        x = [0, 1]
        y = int(input())
        while y > 60 or y < 0:
            y = int(input())
        for i in range(y):
            valor = x[i+1] + x[i]
            x.append(valor)
        print(f"Fib({y}) = {x[y]}")
    except EOFError:
        break
