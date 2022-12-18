n = input('Diga o nome de uma cidade: ')
s = n.strip().upper().split()[0]
print('A cidade se inicia com Santos') if 'SANTOS' in s else print('A cidade não se inicia com Santos')