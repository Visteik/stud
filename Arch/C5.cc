#include <stdio.h>
#include <climits> // Для INT_MAX

// Функция в точном соответствии с заданием
int safe_mul(int a, int b, bool &overflow) {
    int result;
    
    __asm__ volatile (
        "imull %2, %1\n\t"  // Умножаем: %1 = %1 * %2
        "seto %b0\n\t"      // Записываем флаг переполнения (OF) в байтовый регистр
        : "=q" (overflow),  // %0: байтовый регистр для bool
          "+r" (a)          // %1: регистр для 'a' (вход и выход)
        : "r" (b)           // %2: регистр для 'b'
        : "cc"              // Изменяются флаги
    );
    
    result = a;
    return result;
}

int main() {
    bool overflow;
    int res;

    // Тест 1: Успешное умножение
    res = safe_mul(1000, 2000, overflow);
    if (overflow) {
        printf("1000 * 2000 = %d | Переполнение: Да\n", res);
    } else {
        printf("1000 * 2000 = %d | Переполнение: Нет\n", res);
    }

    // Тест 2: Переполнение (INT_MAX * 2)
    res = safe_mul(INT_MAX, 2, overflow);
    if (overflow) {
        printf("INT_MAX * 2 = %d | Переполнение: Да\n", res);
    } else {
        printf("INT_MAX * 2 = %d | Переполнение: Нет\n", res);
    }

    return 0;
}