//Вариант 12
#include<stdio.h>
#define N 15
void max_x(int p[], int *max_price, int *max_index) {
    *max_price = p[0];
    *max_index = 0;
    for (int i = 1; i < N; i++) {
        if (p[i] > *max_price) {
            *max_price = p[i];
            *max_index = i;
        }
    }
}
void min_x(int p[], int *min_price, int *min_index){
    *min_price = price[0];
    *min_index = 0;
    for (int i=0; i < N; i++) {
        if (price[i] < *min_price){
             *min_price = price[i];
             *min_index = i;
        }
    }    
}
int main(){
    int price[N] = {100, 102, 105, 103, 98, 96, 99, 104, 110,
        108, 112, 118, 115, 111, 117};


    printf("Макс ццена = %d, на %d день. Мин цена = %d, на %d день", 
        max_price, max_index, min_price, min_index);

    return 0;
}