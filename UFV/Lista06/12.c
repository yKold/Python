// Considere a função int JogaDado(int num_faces) que recebe o número de faces do
// dados e retorna um valor entre 1 e esse número. Crie a função int testaDados() que utilize
// essa função para obter 3 valores: jogar 100 dados de 10 faces (some o total obtido), 50 dados
// de 20 faces (some o total obtido) e 1 dado de 100 faces. Retorne qual das três teve maior valor,
// (retorne 10 se o primeiro for maior, 50 caso seja o segundo ou 100 para o terceiro.

#include <stdio.h>

int JogaDado(int NF){
}

int testaDados(int nTeste, int nFaces){
    int sum = 0;
    for (int i = 0; i < nTeste; i++)
    {
        sum+= JogaDado(nFaces);
    }
    return sum;
}