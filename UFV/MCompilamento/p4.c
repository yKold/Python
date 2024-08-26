// Aloque dinamicamente memória para um vetor de caracteres de tamanho 10 utilizando ponteiros.
// Utilizando a variável ponteiro criada, preencha cada posição do vetor com o caractere (char)
// correspondente à sua posição (‘0’, ‘1’, ‘2’, ..., ‘9’)

#include <stdio.h>
#include <stdlib.h>

int main(){
    int *ponteiro;
    ponteiro = malloc(10 * sizeof(int));
    
    for (int i = 0; i < 10; i++)
    {
        ponteiro[i] = i;
    }
    for (int i = 0; i < 10; i++)
    {   
        printf("%d\n", ponteiro[i]);
    }
    
}
