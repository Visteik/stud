
#include <cstdio>

int add_sub(int a, int b, int c) {
    int result;
    __asm__ volatile (
        "movl %2, %%eax;"   // eax  = a
        "addl %1, %%eax;"   // eax += b   (теперь (a + b))
        "subl %3, %%eax;"   // eax -= c   (теперь (a + b) - c)
        : "=a" (result)                     // выход: result через EAX
        : "b" (b), "c" (a), "d" (c)         // вход:  EBX = b, ECX = a, EDX = c
        : "cc"                              // изменяем флаги
    );
    return result;
}

int main() {
    int a, b, c;
    printf("Введите а б с \n");
    scanf("%d%d%d", &a, &b, &c);
    printf("%d \n", add_sub(a, b, c));
    return 0;
}