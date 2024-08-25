// Elabore um algoritmo crie um vetor de 50 posições em que o vetor tenha os valores
// [1,2,3,...,50]. Em seguida, mostre o somatório dos seus elementos.

#include <stdio.h>

int main(){

    int V[50], sum = 0;

    for (int i = 0; i < 50; i++)
    {
        int val = i+1;
        V[i] = val;
        sum += val;
    }
    
    printf("%d", sum);

    
    return 0;
}