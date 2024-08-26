Considere um programa que possua a seguinte função int somaptr(int a, int *pb); Essa
função recebe um inteiro e um ponteiro e retorna a soma dos dois valores. Sendo int x e int *y
duas variáveis, diga para cada chamada abaixo da função está correta ou errada e justifique.
 int res = somaptr(x, y);
 int res = somaptr(y, x);
 int res = somaptr(&x, &y);
 int res = somaptr(*y, &x);
 int res = somaptr(*y, y);

#include <stdio.h>

    int soma(int a , int *b){
        return a + *b;
    }

int main(){
    int x = 2, *y = &x;
    *y = 10;
    printf("%d, %d", x, *y);
}