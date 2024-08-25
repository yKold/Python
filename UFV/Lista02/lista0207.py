divisor = int(input())
dividendo = int(input())
if divisor == 0:
    print("Divisão não permitida")
else:
    quociente = dividendo/divisor
    resto = dividendo%divisor
    print(quociente, resto)