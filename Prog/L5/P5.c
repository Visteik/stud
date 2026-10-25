//Вариант 12
#include<stdio.h>
#define N 15
// макс денег и день в который был достигнут
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
//мин денег и мин день в который он был достигнут
void min_x(int p[], int *min_price, int *min_index){
    *min_price = p[0];
    *min_index = 0;
    for (int i=0; i < N; i++) {
        if (p[i] < *min_price){
             *min_price = p[i];
             *min_index = i;
        }
    }    
}
//максимальное падение
void max_drawdown(int p[], int *dd_val, int *dd_start, int *dd_end) {
    int cur_max = p[0];
    int cur_max_idx = 0;
    *dd_val = 0;
    *dd_start = 0;
    *dd_end = 0;
    // Если текущая цена выше текущего максимума: обновляем cur_max и cur_max_idx. 
    //Это значит, что мы нашли новый локальный пик, от которого может начаться следующая просадка.
    // Иначе (цена не выше максимума): считаем просадку от последнего максимума до текущей цены: dd = cur_max - p[i]. 
    // Если эта просадка больше ранее найденной максимальной (dd > *dd_val), обновляем результат: записываем величину 
    // просадки и индексы её начала и конца.
    for (int i = 1; i < N; i++) {
        if (p[i] > cur_max) {
            cur_max = p[i];
            cur_max_idx = i;
        } else {
            int dd = cur_max - p[i];
            if (dd > *dd_val) {
                *dd_val = dd;
                *dd_start = cur_max_idx;
                *dd_end = i;
            }
        }
    }
}

void longest_growth(int p[], int *len, int *start, int *end) {
    *len = 1;
    *start = 0;
    *end = 0;

    int cur_len = 1;
    int cur_start = 0;
    // Считаем, что минимально возможный участок—это один элемент (длина 1), и пока считаем, что лучший найденный участок—это первый элемент.
    // cur_len и cur_start—текущие длина и начало текущего растущего отрезка, который мы прямо сейчас «наращиваем».
    // Если цена не упала (p[i] >= p[i-1]): текущий растущий отрезок продолжается, просто увеличиваем его длину: cur_len++.
    // Если цена упала (p[i] < p[i-1]): растущий отрезок прервался.
    // Сначала проверяем, не стал ли текущий отрезок самым длинным из всех, что мы видели: если cur_len > *len, 
    // обновляем лучший результат (*len, *start, *end). Конец текущего отрезка — это i - 1, потому что на индексе i рост уже нарушился.
    // Затем начинаем новый отрезок: длина снова 1, а его начало — текущий индекс i.
    for (int i = 1; i < N; i++) {
        if (p[i] >= p[i-1]) {
            cur_len++;
        } else {
            if (cur_len > *len) {
                *len = cur_len;
                *start = cur_start;
                *end = i - 1;
            }
            cur_len = 1;
            cur_start = i;
        }
    }

    if (cur_len > *len) {
        *len = cur_len;
        *start = cur_start;
        *end = N - 1;
    }
}

int main(){
    int price[N] = {100, 102, 105, 103, 98, 96, 99, 104, 110,
        108, 112, 118, 115, 111, 117};

    int max_price, max_index;
    int min_price, min_index;
    int dd_val, dd_start, dd_end;
    int len, start, end;

    max_x(price, &max_price, &max_index);
    min_x(price, &min_price, &min_index);
    max_drawdown(price, &dd_val, &dd_start, &dd_end);
    longest_growth(price, &len, &start, &end);

    printf("Макс цена = %d, на %d день. Мин цена = %d, на %d день\n",
           max_price, max_index + 1, min_price, min_index + 1);
    printf("Максимальная просадка = %d руб. (начало - день %d, конец - день %d)\n",
           dd_val, dd_start + 1, dd_end + 1);
    printf("Самый длинный период роста = %d дней (дни %d - %d)\n",
           len, start + 1, end + 1);
        
    return 0;
}