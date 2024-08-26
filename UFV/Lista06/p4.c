// Aloque dinamicamente memória para um vetor de caracteres de tamanho 10 utilizando ponteiros.
// Utilizando a variável ponteiro criada, preencha cada posição do vetor com o caractere (char)
// correspondente à sua posição (‘0’, ‘1’, ‘2’, ..., ‘9’)

#include <stdlib.h>

int main(){
    char *vetor;
    vetor = malloc(10 * sizeof(char));

    for(int i = 0; i < 10; i++){
        vetor[i] = '0' + i;
    }
    free(vetor);
    return 0;
}

