// Escreva uma função que receba como parâmetros um vetor de inteiros e seu tamanho, sua
// função deve retornar o valor médio do vetor

#include <stdio.h>

int media(int V[], int tam){
    int res = 0;
    for (int i = 0; i < tam; i++)
    {
        res += V[i];
    }
    return res;
}
