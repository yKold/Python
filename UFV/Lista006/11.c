// Crie uma função que receba 4 parâmetros inteiros: hora1, minutos1, e hora2, minutos2 que
// representam duas horas do dia. Sua função deve sua função deve retornar a diferença total em
// minutos entre os dois horários.


int sobra(int h1, int m1, int h2, int m2){
    int T1 = m1 + (h1 * 60), T2 = m2 + (h2 * 60), res;
    if (T1 > T2)
    {
        res = T1 - T2;
    }
    else if (T2 > T1)
    {
        res = T2 - T1;
    }
    else{
        res = 0;
    }
    
    return  res;
}
