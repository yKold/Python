// Escreva uma função que receba como parâmetros dois ponteiros para float e troque os valores
// apontados pelos ponteiros.

void Troca(float *a, float *b){
    float aux = *a;
    *a = *b;
    *b = aux;
    printf("%f, %f", *a, *b);
}
