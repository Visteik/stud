#include <stdio.h>

// Функция находит 3 самых частых символа (кроме пробела).
// top_chars  — массив минимум на 3 элемента для символов
// top_counts — массив минимум на 3 элемента для их частот
// Возвращает реальное количество найденных уникальных символов (0..3).
int get_top3_chars(const char *str, char *top_chars, int *top_counts) {

    // 1. Подсчет частот всех символов, кроме пробела
    int count[256] = {0};
    for (int i = 0; str[i] != '\0'; i++) {
        unsigned char c = (unsigned char)str[i];
        if (c == ' ') continue;
        count[c]++;
    }

    // 2. Инициализация топ-3 нулями
    for (int i = 0; i < 3; i++) {
        top_chars[i]  = 0;
        top_counts[i] = 0;
    }

    // 3. Один проход по массиву count — поддерживаем топ-3
    for (int i = 0; i < 256; i++) {
        if (count[i] == 0) continue;

        if (count[i] > top_counts[0]) {
            top_counts[2] = top_counts[1];  top_chars[2] = top_chars[1];
            top_counts[1] = top_counts[0];  top_chars[1] = top_chars[0];
            top_counts[0] = count[i];       top_chars[0] = (char)i;
        } else if (count[i] > top_counts[1]) {
            top_counts[2] = top_counts[1];  top_chars[2] = top_chars[1];
            top_counts[1] = count[i];       top_chars[1] = (char)i;
        } else if (count[i] > top_counts[2]) {
            top_counts[2] = count[i];       top_chars[2] = (char)i;
        }
    }

    // 4. Подсчитываем, сколько реально символов нашли
    int found = 0;
    for (int i = 0; i < 3; i++) {
        if (top_counts[i] > 0) found++;
    }
    return found;
}

int main() {
    const char *str = "the quick brown fox jumps over the lazy dog";

    char top_chars[3];
    int  top_counts[3];

    int found = get_top3_chars(str, top_chars, top_counts);

    printf("Строка: \"%s\"\n\n", str);
    printf("Топ-%d самых частых символов (без пробелов):\n", found);

    for (int i = 0; i < found; i++) {
        printf("%d. '%c' (ASCII %d) — %d раз(а)\n",
               i + 1,
               top_chars[i],
               (unsigned char)top_chars[i],
               top_counts[i]);
    }

    return 0;
}