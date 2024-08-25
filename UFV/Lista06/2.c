// Escreva um programa que leia do teclado valores para um vetor de 20 posições. Depois
// imprima qual é o maior e mostre também em qual posição ele se encontra.

#include <stdio.h>

int maior(int n[], int tam){
    n[tam];
    for (int i = 0; i < tam-1; i++)
    {
        for (int j = 0; j < tam-1; j++)
        {
            if(n[j+1] < n[j]){
                int aux = n[j+1];
                n[j+1] = n[j];
                n[j] = aux;
            }
        }
    }
    return n[tam-1];
}
int main(){

    int V[20], x, Z[20];

    for (int i = 0; i < 20; i++)
    {
        scanf("%d", &x);
        Z[i] = x;
        V[i] = x;
    }
    int y = maior(V, 20);
    
    for (int i = 0; i < 20; i++)
    {
        if(Z[i] == y){
            printf("%d, %d", y, i);
        }
    }
    
    return 0;
}