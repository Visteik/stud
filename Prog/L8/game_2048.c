/**
n - размер поля
** board - само поле размера n*n
test_error - проверка на ошибку выделения памяти
test_board вывод поля
spawn_title - пустые клетки занимает 2 или 4








не сделаны score для запсии счета(уже есть для подсчтеа в слиянии)
не сделана diretion для запис получаемого символа 
 */
#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int test_error(void* test){
    if (test == NULL){
        printf("Ошибка выделения памяти!\n");
        return(1);
    }
    return(0);
}

void test_board(int** board, int n){
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            printf("%d ", board[i][j]);
        }
        printf("\n");
    }
}

void spawn_title(int** board, int n){
    int empty_count = 0; //счетчик пустых клеток на поле
    for (int i = 0; i < n; i++){
        for (int j =0 ; j < n; j++){
            if (board[i][j] == 0){
                empty_count++;
            }
        }
    }
    if (empty_count == 0){
        return;
    }
    int idx = rand()%empty_count;
    for (int i = 0; i < n; i++){
        for (int j =0 ; j < n; j++){
            if (board[i][j] == 0){
                if (idx == 0){
                int roll = rand() % 100;
                board[i][j] = (roll < 90) ? 2 : 4;
                return;
            }
            idx--;
            }
            
        }
    }
}

void shift_row_left(int* row, int n, int* score){
    //сжатие влево
    int pos = 0;
    for (int i = 0; i < n; i++){
        if (row[i] != 0){
            row[pos] = row[i];
            if (i != pos){
                row[i] = 0;
            }
        pos++;
        }
        
    }
    //слияние одинаковых
    for(int i = 0; i < n-1; i++){
        if (row[i] == row[i+1]){
            row[i] *= 2;
            row[i+1] = 0;
            *score += row[i];
            i++; 
        }
    }
    //снова сжимает
    pos = 0;
    for (int i = 0; i < n; i++){
        if (row[i] != 0){
            row[pos] = row[i];
            
            if (i != pos){
                row[i] = 0;
            }
        pos++;    
        }
        
    }  
    // Тест
    // for (int i = 0; i <n; i++){
    //     printf("%d \n", row[i]);
    // }  
}

void reverse_row(int* row, int n){
    for (int i=0; i < n/2; i++){
        int t = row[i];
        row[i] = row[n-1-i];
        row[n-1-i] = t;
    }

}

void transpose(int** board, int n){
    
    for (int i =0; i < n; i++){
        for (int j = i + 1; j < n; j++){
            int t = board[i][j];
            board[i][j] = board[j][i];
            board[j][i] = t;
        }
    }
}



void shift_left(int** board, int n, int* score){
    for (int i = 0; i <n; i++){
        shift_row_left(board[i], n, score);
}
}

void process_move(int** board, int n, int* score, char direction){
    if(direction == 'a'){
        shift_left(board, n, score);

    } else if(direction == 'd'){
        for (int i = 0; i < n; i++) reverse_row(board[i], n);
        shift_left(board, n, score);
        for (int i = 0; i < n; i++) reverse_row(board[i], n);

    }else if(direction == 'w'){
        transpose(board, n);
        shift_left(board, n, score);
        transpose(board, n);

    }else if(direction == 's'){
        transpose(board, n);
        for (int i = 0; i < n; i++) reverse_row(board[i], n);
        shift_left(board, n, score);
        for (int i = 0; i < n; i++) reverse_row(board[i], n);
        transpose(board, n);
    }

}

int is_game_over(int** board, int n){
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (board[i][j] == 0) return 0;

        }

    }
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (j < n-1 && board[i][j] == board [i][j+1]) return 0;
            if (i < n-1 && board[i][j] == board [i+1][j]) return 0;

        }

    }    
    return 1;
}

void copy_board(int** board, int** last_board, int n){
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){    
            last_board[i][j] = board[i][j];
        }
    }        
}

int srav_board(int** board, int** last_board, int n){
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){    
            if(board[i][j] != last_board[i][j]){
                return 0;
            }
        }
    }   
    return 1;
}



void save_history(int** board, int* score, int n, int** history, int* history_count){

    int one_size = n*n + 1; //Размер одного состояния nn поле + 1 на счет
    int* new_history = (int*)realloc(*history, (*history_count + 1)*one_size*sizeof(int));
    if (test_error(new_history)) return;
    *history = new_history;
    // проверяем следующий свободный индекс
    int offset = (*history_count)* one_size;
    for(int i =0; i <n; i++){
        for(int j = 0; j < n; j++){
            (*history)[offset+i*n+j] = board[i][j];
        }
    }
    //записываем счет в последний элемент
    (*history)[offset+n*n] = *score;
    (*history_count)++;
}

void undo_move(int** board, int* score, int n, int** history, int* history_count){
    if (*history_count == 0){
        printf("История пустая \n");
        return;
    } 
    (*history_count)--;
    int one_size = n*n + 1;
    int offset = (*history_count)* one_size;

    for(int i =0; i <n; i++){
        for(int j = 0; j < n; j++){
            board[i][j] = (*history)[offset+i*n+j];
        }
    }
    *score = (*history)[offset+n*n];
    printf("Ход отменен \n");
}



int main(){
    srand(time(NULL));
    int n;
    printf("Введите размера поля: \n");
    scanf("%d", &n);
    
    if (n <= 1){
        printf("Некорректный размер поля\n");
        return 1;
    }
    int **board = (int**)calloc(n, sizeof(int*));
    int **last_board = (int**)calloc(n, sizeof(int*));
    
    if (test_error(board)) return 1;
    
    for (int i = 0; i < n; i++){
        board[i] = (int*)calloc(n, sizeof(int));
        last_board[i] = (int*)calloc(n, sizeof(int));
        if (test_error(board[i]) || test_error(last_board[i])) return 1;
    }
    
    int score = 0;

    int* history = NULL;
    int history_count = 0;


    printf("можно играть w a s d для движения, q - завершить игру. \n");
    spawn_title(board, n);
    spawn_title(board, n);
    while(1){
        system("clear");
        test_board(board, n);
        printf("Счет: %d\n", score);

        
        if (is_game_over(board, n)){
            printf("Ты лузер, кек. Счет: %d \n", score);
            break;
        }

        char move;
        scanf(" %c", &move);

        if (move == 'q') break;
        


        if (move == 'r'){
            undo_move(board, &score, n, &history, &history_count);
            continue;
        }

        int old_score = score;
        copy_board(board, last_board, n);

        process_move(board, n, &score, move);

        if (!srav_board(board, last_board, n)){
            save_history(last_board, &old_score, n, &history, &history_count);
            spawn_title(board, n);
        }else{
            printf("ход ничего не меняет \n");
            score = old_score;
        }


    }
    for (int i = 0; i < n; i++) {
        free(board[i]);
        free(last_board[i]);
    }
    free(board);
    free(last_board);
    free(history);


    return 0;
}