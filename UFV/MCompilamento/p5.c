// Escreva um programa que peça ao usuário que digite um valor inteiro N e, em seguida, declare
// dinamicamente um vetor (usando malloc) de inteiros de tamanho N e preencha-o com 0s. Utilize um
// ponteiro para percorrer o vetor (Não utilize colchetes)
#include <stdio.h>
#include <stdlib.h>

int main(){
    int N;
    scanf("%d", &N);

    int *ponteiro = (int*)malloc( N * sizeof(int));
    for (int i = 0; i < N; i++)
    {
        *(ponteiro+1) = 0;
    }
     
    return 0;
}