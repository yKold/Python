// Agora escreva uma função que receba como parâmetro esse vetor de ponteiros de inteiros e o seu
// tamanho e sua função retorne a soma dos valores apontados deste vetor.


int Soma(int *ponteiros[], int tam){
    int sum = 0;
    for (int i = 0; i < tam; i++)
    {
        sum += *ponteiros[i];
    }
    return sum;
}
