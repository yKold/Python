#include <stdio.h>

int main() {

    int a,b;
    double c;

    scanf("%i", &a);
    scanf("%i", &b);
    scanf("%lf", &c);

    double salary = c * b;

    printf("NUMBER = %i\nSALARY = U$ %.2lf\n", a, salary);

    return 0;
}