#include <stdio.h>

int main(){

    double a;
    scanf("%lf", &a);

    if ( 0 < a && a <= 2000 ) 
    {
        printf("Isento");
    } else if ( 2000.01 < a && a <= 3000 )
    {
        double b = a*0.08;
        printf("R$ %.2lf", b);
    } else if ( 3000.01 < a && a <= 4500)
    {
        double b = a*0.18;
        printf("R$ %.2lf", b);
    } else 
    {
        double b = a*0.28;
        printf("R$ %.2lf", b);
    }
    
    
    return 0;
}