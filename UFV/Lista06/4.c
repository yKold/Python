// Considerando a série abaixo, escreva um algoritmo que seja capaz de gerar seus N termos.
// Esse número N deve ser lido do teclado.
// S = 1,4,4,2,5,5,3,6,6,4,7,7...

#include <stdio.h>

int main(){

    int x = 1, y = 4, n;
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        printf("%d, %d, %d, ", x, y, y);
        x++;
        y++;
    }
    
    return 0;
}