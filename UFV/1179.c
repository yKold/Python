// #include <stdio.h>

// int main(){

//     int Par[5], Impar[5];
//     int num, cPar = 0, cImpar = 0;

//     for(int i = 0; i <= 15; i++){
//         scanf("%d", &num);
//         if(num % 2 == 0){
//             if(sizeof(Par)/sizeof(int) < 5){
//                 Par[cPar] = num;
//                 cPar++;
//             }
//             else{
//                 for(int j=0; j <=5; j++){
//                     printf("TEste%d", Par[i]);
//                 }
//                 cPar = 0;
//             }
//         }
//         else{
//             // Impar[cImpar] = num;
//             cImpar++;
//         }
//     }
//     for(int i = 0; i < sizeof(Par)/sizeof(int); i++){
//         printf("%d\n", Par[i]);
//         // printf("%d\n", Impar[i]);
//     }

//     return 0;
// }

#include <stdio.h>

#define SIZE 5

void printVector(const char* label, int *vector, int count) {
    for (int i = 0; i < count; i++) {
        printf("%s[%d] = %d\n", label, i, vector[i]);
    }
}

int main() {
    int pares[SIZE], impares[SIZE];
    int countPares = 0, countImpares = 0;
    int num;

    // Ler 15 números inteiros
    for (int i = 0; i < 15; i++) {
        scanf("%d", &num);

        if (num % 2 == 0) {
            // Número é par
            pares[countPares] = num;
            countPares++;
            if (countPares == SIZE) {
                printVector("par", pares, SIZE);
                countPares = 0; // Reiniciar o vetor de pares
            }
        } else {
            // Número é ímpar
            impares[countImpares] = num;
            countImpares++;
            if (countImpares == SIZE) {
                printVector("impar", impares, SIZE);
                countImpares = 0; // Reiniciar o vetor de ímpares
            }
        }
    }

    // Imprimir quaisquer valores restantes no vetor de ímpares
    if (countImpares > 0) {
        printVector("impar", impares, countImpares);
    }

    // Imprimir quaisquer valores restantes no vetor de pares
    if (countPares > 0) {
        printVector("par", pares, countPares);
    }

    return 0;
}
