#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Функция вычисления определителя матрицы
double determinant(double *matrix, int n) {
    if (n == 1) {
        return matrix[0];
    }
    
    if (n == 2) {
        return matrix[0] * matrix[3] - matrix[1] * matrix[2];
    }
    
    double det = 0;
    double *submatrix = malloc((n-1) * (n-1) * sizeof(double));
    
    for (int col = 0; col < n; col++) {
        // Создание подматрицы
        int sub_i = 0;
        for (int i = 1; i < n; i++) {
            int sub_j = 0;
            for (int j = 0; j < n; j++) {
                if (j != col) {
                    submatrix[sub_i * (n-1) + sub_j] = matrix[i * n + j];
                    sub_j++;
                }
            }
            sub_i++;
        }
        
        double sign = (col % 2 == 0) ? 1 : -1;
        det += sign * matrix[col] * determinant(submatrix, n-1);
    }
    
    free(submatrix);
    return det;
}

// Алгоритм Крамера
void cramers_rule(double *A, double *b, double *x, int n) {
    double det_A = determinant(A, n);
    
    if (fabs(det_A) < 1e-10) {
        printf("Определитель равен нулю! Система не имеет единственного решения.\n");
        return;
    }
    
    double *A_modified = malloc(n * n * sizeof(double));
    
    for (int i = 0; i < n; i++) {
        // Копирование исходной матрицы
        for (int j = 0; j < n * n; j++) {
            A_modified[j] = A[j];
        }
        
        // Замена i-го столбца на вектор b
        for (int j = 0; j < n; j++) {
            A_modified[j * n + i] = b[j];
        }
        
        // Вычисление xi = det(Ai) / det(A)
        x[i] = determinant(A_modified, n) / det_A;
    }
    
    free(A_modified);
}

int main() {
    int n;
    
    printf("Введите размерность системы N: ");
    scanf("%d", &n);
    
    // Выделение памяти
    double *A = malloc(n * n * sizeof(double));
    double *b = malloc(n * sizeof(double));
    double *x = malloc(n * sizeof(double));
    
    // Ввод матрицы коэффициентов
    printf("\nВведите матрицу коэффициентов A (%dx%d):\n", n, n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("A[%d][%d] = ", i, j);
            scanf("%lf", &A[i * n + j]);
        }
    }
    
    // Ввод вектора свободных членов
    printf("\nВведите вектор свободных членов b:\n");
    for (int i = 0; i < n; i++) {
        printf("b[%d] = ", i);
        scanf("%lf", &b[i]);
    }
    
    // Решение системы
    cramers_rule(A, b, x, n);
    
    // Вывод результата
    printf("\nРешение системы:\n");
    for (int i = 0; i < n; i++) {
        printf("x[%d] = %lf\n", i, x[i]);
    }
    
    // Освобождение памяти
    free(A);
    free(b);
    free(x);
    
    return 0;
}