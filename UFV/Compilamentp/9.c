// Escreva uma função que receba uma string (um vetor de caracteres). Sua função deve
// imprimir a string na tela e retornar o tamanho dessa string.

#include <stdio.h>

void retornar(char C[]){
    int count = 0;
    while (C[count] != '\0')
    {
        printf("%c", C[count]);
        count++;
    }
    printf("%d", count);
}

int main(){
    char C[8] = {"Gabriel"};
    retornar(C);
    return 0;
}