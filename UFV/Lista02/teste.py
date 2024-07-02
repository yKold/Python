num_guardados = []
resultado = []
range_max = 0

for i in range(100):
    x = int(input())
    num_guardados.append(x)

for i in num_guardados:
        if i > range_max:
            range_max = i
            
for i in range(range_max+1):
    for j in num_guardados:
        if i == j:
            resultado.append(i)

print(resultado)

         
