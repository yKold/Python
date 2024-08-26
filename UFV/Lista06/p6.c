#include <stdio.h>
#include <stdlib.h>

int main() {
    // Declarar um vetor de ponteiros para inteiros de tamanho 10
    int *vetor[10];

    // Preencher o vetor com ponteiros alocados dinamicamente
    for (int i = 0; i < 10; i++) {
        vetor[i] = (int *)malloc(sizeof(int)); // Aloca memória para um inteiro
        if (vetor[i] == NULL) {
            printf("Erro na alocação de memória para vetor[%d]\n", i);
            return 1;
        }
        *vetor[i] = i + 1; // Atribuir um valor ao inteiro alocado (opcional)
    }

    // Exibir os valores armazenados e os endereços de memória
    for (int i = 0; i < 10; i++) {
        printf("vetor[%d] = %d, endereço = %p\n", i, *vetor[i], (void *)vetor[i]);
    }

    // Liberar a memória alocada
    for (int i = 0; i < 10; i++) {
        free(vetor[i]);
    }

    return 0;
}
