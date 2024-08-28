// Escreva uma função que receba como parâmetro um ponteiro para uma string e um caractere. Sua
// função deve substituir todas as ocorrências deste caractere no array pelo caractere de espaço em
// branco.
#include <stdio.h>
void Substituir(char *Vetor[], char C){
    for (int i = 0; *Vetor[i] != '\0'; i++)
    {
        if (*Vetor[i] == C)
        {
            *Vetor[i] = ' ';
        }
        
    }
    for (int i = 0; *Vetor[i] != '\0'; i++)
    {   
        printf("%d", *Vetor[i]);
    }
    
    
}

int main(){
    char *Batata[7] = {'b','a','t','a','t','a'};
    char a = 'a';
    Substituir(Batata, a);
    return 0;
}