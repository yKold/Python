#include <stdio.h>

int main(){
    
    char nome[50];
    double a,b;
    double total;

    scanf("%49s", nome);
    scanf("%lf", &a);
    scanf("%lf", &b);

    total = a + (b * 0.15);

    printf("TOTAL = R$ %.2lf\n", total);

    return 0;
}