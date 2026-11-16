#include <cstdio>

unsigned int factorial(unsigned int n) { 
    unsigned int result; 
        __asm__ ( 
            "movl %1, %%ecx;"   
            "movl $1, %%eax;"   
            "cmp $0, %%ecx;" 
            "je 2f;"            
            "1:;" 
            // n в ecx 
            // result = 1 
            // если n==0, выход 
            "imul %%ecx, %%eax;" // eax *= ecx 
            "loop 1b;"          
            // декремент ecx и переход, пока ecx != 0 
            "2:;" 
            : "=a" (result) 
            : "r" (n) 
            : "ecx", "cc" 
    ); 
    return result; 
}

int main() {
    printf("0! = %u\n", factorial(0));
    printf("1! = %u\n", factorial(1));
    printf("5! = %u\n", factorial(5));
    return 0;
}