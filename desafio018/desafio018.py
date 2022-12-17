import math

n = float(input('Qual o ângulo? '))

sen = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tan = math.tan(math.radians(n))

print('O seno, cosseno e tangente do seu ângulo são respectivamente {:.2f} , {:.2f} e {:.2f}.'.format(sen, cos, tan))