# def lin(msg):
#     print('_' * 30)
#     print(msg)
#     print('-' * 30)

# lin("eu sou lindo pra krlh")
#################################
# def soma(a, b):
#     return print(a+b) 

# soma(10, 2)
#################################

# def contador(*num):
#     print(num)

# contador(1,2,3,4)
#################################

def soma(*valores):
    s = 0
    for i in valores:
        s += i
    print(s)

soma(1,2,3,4)