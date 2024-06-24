
from math import floor
x = int(input()) / 30 / 12

resano = floor(x)
rano = x - resano

rmes = rano * 12
resmes = floor(rmes)

rdia = (rmes - resmes) * 30
resdia = floor(rdia)

print(resano, resmes, resdia)
