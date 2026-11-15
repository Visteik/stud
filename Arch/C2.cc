#include <cstdio>

void swap(int *x, int *y) { 
    int tmp; 
        __asm__ ( 
            "movl (%2), %%eax;"   
            "movl (%3), %%ebx;"   
            "movl %%ebx, (%2);"   
            "movl %%eax, (%3);"   
            // eax = *x 
            // ebx = *y 
            // *x = ebx 
            // *y = eax 
            : "=m" (*x), "=m" (*y)   // помечаем как изменяемые 
            : "r" (x), "r" (y)       
            // регистры с указателями 
            : "eax", "ebx", "memory" 
        ); 
} 

int main() {
    int a = 5, b = 10;
    printf("До: a = %d, b = %d\n", a, b);
    swap(&a, &b);
    printf("После: a = %d, b = %d\n", a, b);
    return 0;
}