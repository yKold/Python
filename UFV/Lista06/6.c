// Faça um programa que crie um vetor de tamanho 25 preenchido com valores informados
// pelo teclado, e depois inverta a ordem do vetor (sem utilizar um segundo vetor)

#include <stdio.h>

int main(){
    int val = 25;
    int V[val];
    for (int i = 0; i < val; i++)
    {
        int x;
        scanf("%d", &x);
        V[i] = x;
    }
    for (int i = 0; i < 12; i++)
    {
        int aux = V[i];
        V[i] = V[24-i];
        V[24-i] = aux;
    }
    return 0;
}