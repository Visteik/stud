#include<stdio.h>
#include <stdlib.h>
#include <time.h>


int main(){
    int N;
    printf("Введите размер масси1ва: \n");
    scanf("%d", &N);
    double real[N];
    double mnim[N];
    srand(time(NULL));

    for (int i=0; i < N; i++) {
        real[i] = rand()%65536-32768;
        mnim[i] = rand()%65536-32768;
    }
    for (int i =0; i <N; i++){
        printf("%.1f  %.1f \n", real[i], mnim[i]);
    }
    for (int i=0; i < N; i++) {
        printf("s[%d] = %.1f + j*(%.1f)\n", i, real[i], mnim[i]);
    }
    double eng = 0.0;
    for (int i=0; i < N; i++) {
        eng += real[i]*real[i] + mnim[i]*mnim[i];
    }
    printf("Энергия сигнала = %.1f \n", eng);
    double max_real = real[0];
    int max_index = 0;
    for (int i=0; i < N; i++) {
        if (real[i] > max_real){
             max_real = real[i];
             max_index = i;
        }
    }
    printf("Максимальный элемент реальной части: %.1f (индекс %d)\n", max_real, max_index);
    return 0;
}