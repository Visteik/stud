#include<stdio.h>
#include<stdlib.h>


void zapolnenie(double **orig_matrix, int *size_matrix)
    printf("Введите каждую строку матрицы форматом: x1 x2 x3 ... xN число_после_равно");
    for (int i = 0; i < size_matrix; i++) {
        for (int j = 0; j < size_matrix; j++) {
            scanf("%lf", &orig_matrix[i][j]);
        }
    }
void copy_matrix(double **orig_matrix, int *size_matrix,double **matrix_cp)
    for (int i = 0; i < n; ++i){
        for (int j = 0; j < n; ++j){
            matrix_cp[i][j] = orig_matrix[i][j];
        }
}


int main() {
int size_matrix, m;

printf("Введите количество уравнений и неизвестных в формате: 5 5 \n");
scanf("%d %d", &size_matrix, &m);
//Тест на дебила
if (N != m) {
    printf("Матрица не квадратная, метод Крамера неприменим \n");
}


// сама программа
else{
    //создаем матриу динамического размера
    double **orig_matrix = malloc(size_matrix * sizeof(double*));
    for (int i = 0; i < size_matrix; ++i)
        orig_matrix[i] = malloc(size_matrix * sizeof(double));
    //заполняем матрицу
    zapolnenie(orig_matrix, &size_matrix);
    //создаем матрицу для копирования оригинальной
    double **matrix_cp = malloc(size_matrix * sizeof(double*));
    for (int i = 0; i < size_matrix; ++i)
        matrix_cp[i] = malloc(size_matrix * sizeof(double));
    //копируем матрицу
    copy_matrix(orig_matrix, &size_matrix, matrix_cp)

}
for (int i = 0; i < size_matrix; i++) {
    for (int j = 0; j < size_matrix; j++) {
        printf("%.1lf ", orig_matrix[i][j]);
    }
    printf("\n"); // в конце строки - перевод на новую
}
}







return 0;
}