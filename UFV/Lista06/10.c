// Escreva uma função que receba como parâmetros 3 inteiros diferentes. Sua função deve
// imprimir os três números em ordem crescente. Note que sua função só deve imprimir e não tem
// nenhum valor de retorno.

void retornar(int a, int b, int c){
    int V[3] = {a, b, c};
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            if (V[i+1] < V[i])
            {
                int aux = V[i];
                V[i] = V[i+1];
                V[i+1] = aux;
            }
        }
    }
    for (int i = 0; i < 3; i++)
    {
        printf("%d\n", V[i]);
    }
    
}
