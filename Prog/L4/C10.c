#include <stdio.h>

int print_bin_n(int dec) {
    
    int bit_0 = 0;

    for (int i = 12; i >= 2; i--) {
        //printf("%d \n", i);
        if (((dec >> i) & 1) == 0) {
            bit_0++;
        }
    }
    printf("%d \n", bit_0);
}

int main() {
    int number;
    printf("Введите целое число: \n");
    scanf("%d", &number);
    print_bin_n(number);







return 0;
}