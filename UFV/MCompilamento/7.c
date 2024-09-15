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


int Funcao(int a, int b){
    if (b == 1)
    {
        return a;
    }
    else{
        return a * Funcao(a, b-1);
    }
}

int Fatorial(int a){
    if(a == 1){
        return 1;
    }
    else{
        return a * Fatorial(a-1);
    }
}

int main(){
    printf("%d\n", Funcao(2,3));
    printf("%d", Fatorial(5));
    return 0;
}