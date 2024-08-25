#include <stdio.h>

int main(){


double Salary;
scanf("%lf", &Salary);
double Taxa = 0;

if (Salary > 0 && Salary <= 2000){
    Taxa = 999;
    if (Taxa == 999){
        printf("Isento\n");
} 
}
else if (Salary > 2000 && Salary <= 3000){
    Salary -= 2000;
    Taxa = 0.08;
    Salary *= Taxa;
    printf("R$ %.2lf\n", Salary);
}
else if (Salary > 3000 && Salary <= 4500){
    Salary -= 3000;
    Taxa = 0.18;
    Salary *= Taxa;
    Salary += 1000*0.08;
    printf("R$ %.2lf\n", Salary);
}
else{
    Salary -= 4500;
    Taxa = 0.28;
    Salary *= Taxa;
    Salary += 1500 * 0.18;
    Salary += 1000 * 0.08;
    printf("R$ %.2lf\n", Salary);
}

    return 0;
}