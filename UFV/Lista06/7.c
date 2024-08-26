// Escreva uma função que receba dois valores inteiros A e B e calcule a potência de A
// (número real) por B (número inteiro e positivo), ou seja, AB
//  (A elevado a B), através de
// multiplicações sucessivas. Sua função deve retornar o resultado obtido
#include <stdio.h>

int pot(int x, int y){
    int res = x;
    for (int i = 1; i < y; i++)
    {
        res *= x;
    }
    
    return res;
}

