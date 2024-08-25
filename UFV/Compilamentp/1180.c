#include <stdio.h>

int main(){

    int N;
    scanf("%d", &N);
    int Vetor[N];
    for(int i=0; i < N; i++){
        scanf("%d", &Vetor[i]);
    }
    int menor = Vetor[0], pos = 0;

    for(int j=0; j < N-1; j++){
        if(Vetor[j+1] < menor){
            menor = Vetor[j+1];
            pos = j+1;
        }
    }
    printf("Menor valor: %d\nPosicao: %d\n", menor, pos);

    return 0;
}