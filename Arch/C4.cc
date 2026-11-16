#include <cstdio>

int sum_array(const int *arr, size_t len) {
    int sum;
    __asm__ (
        "movl %1, %%esi;" // arr
        "movl %2, %%ecx;" // len
        "xorl %%eax, %%eax;" // sum = 0
        "test %%ecx, %%ecx;"
        "jz 2f;"
        "1:;"
        "addl (%%esi), %%eax;"
        "addl $4, %%esi;" // переходим к следующему элементу
        "loop 1b;"
        "2:;"
        : "=a" (sum)
        : "r" (arr), "r" (len)
        : "esi", "ecx", "cc"
    );
    return sum;
}

int main() {
    int my_arr[] = {10, 20, 30, 40};
    size_t n = sizeof(my_arr) / sizeof(my_arr[0]);
    printf("Сумма: %d\n", sum_array(my_arr, n)); // Ожидается 100
    return 0;
}