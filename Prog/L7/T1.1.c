
#include <stdio.h>
#include <ctype.h>
#include <string.h>

// Функция преобразует имя в ник и возвращает количество заменённых пробелов
int make_nickname(const char *name, char *nickname, size_t nick_size) {
    int space_count = 0;
    size_t j = 0;  // индекс для результирующего ника

    for (size_t i = 0; name[i] != '\0' && j + 1 < nick_size; ++i) {
        unsigned char ch = (unsigned char)name[i];

        if (ch == ' ') {
            nickname[j++] = '_';
            space_count++;
        } else if (isalpha(ch)) {
            // Буквы переводим в нижний регистр
            nickname[j++] = (char)tolower(ch);
        } else {
            // Если вдруг есть другие символы (не буквы и не пробелы),
            // можно либо пропускать, либо копировать — тут пропускаем
            continue;
        }
    }

    nickname[j] = '\0';  // завершающий ноль
    return space_count;
}

int main() {
    char name[] = "Marat Pahmutov";
    // Буфер для ника: размер имени + запас (на случай, если пробелы станут подчёркиваниями той же длины)
    char nickname[100];

    int spaces_replaced = make_nickname(name, nickname, sizeof(nickname));
    size_t nick_len = strlen(nickname);

    printf("Ник: %s\n", nickname);           // marat_pahmutov
    printf("Длина ника: %zu\n", nick_len);   // 15
    printf("Пробелов заменено: %d\n", spaces_replaced);  // 1

    return 0;
}