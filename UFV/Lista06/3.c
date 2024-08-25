// Escreva um programa que leia do teclado um número de um mês e imprima o nome do mês
// equivalente, se o número for menor ou igual a zero ou maior que 6, imprima que o número
// do mês é inválido. (Obsevação: utilize neste exercício o comando “switch” para resolver o
// mês. Pode fazer apenas com os meses de Janeiro a Junho!)

#include <stdio.h>

int main(){
    int mes;
    scanf("%d", &mes);

    switch (mes)
    {
    case 1:
        printf("Janeiro");
        break;
    case 2:
        printf("Fevereiro");
        break;
    case 3:
        printf("Março");
        break;
    case 4:
        printf("Abril");
        break;
    case 5:
        printf("Maio");
        break;
    case 6:
        printf("Junho");
        break;
    
    default:
        printf("Inválido");
        break;
    }

    return 0;
}