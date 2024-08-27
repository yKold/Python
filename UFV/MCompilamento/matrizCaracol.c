#include <stdio.h>

int main() {
    int n;
    printf("Digite o tamanho da matriz (n x n): ");
    scanf("%d", &n);

    int matrix[n][n];
    int value = 1;
    int top = 0, bottom = n - 1, left = 0, right = n - 1;

    while (value <= n * n) {
        // Preencher da esquerda para a direita na linha superior
        for (int i = left; i <= right && value <= n * n; i++) {
            matrix[top][i] = value++;
        }
        top++;

        // Preencher de cima para baixo na coluna direita
        for (int i = top; i <= bottom && value <= n * n; i++) {
            matrix[i][right] = value++;
        }
        right--;

        // Preencher da direita para a esquerda na linha inferior
        for (int i = right; i >= left && value <= n * n; i--) {
            matrix[bottom][i] = value++;
        }
        bottom--;

        // Preencher de baixo para cima na coluna esquerda
        for (int i = bottom; i >= top && value <= n * n; i--) {
            matrix[i][left] = value++;
        }
        left++;
    }

    // Imprimir a matriz caracol
    printf("Matriz caracol:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%3d ", matrix[i][j]);
        }
        printf("\n");
    }

    return 0;
}
