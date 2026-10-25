#include <stdio.h>
#include <ctype.h>
#include <string.h>
int del_space(const char *text, char *ver_text, size_t text_size){
    int space_count = 0;
    size_t j = 0;
    for (size_t i = 0; text[i] != '\0' && j + 1 < text_size; i++){
        unsigned char ch = (unsigned char)text[i];
        

        if (ch == ' '){
            if (text[i-1] == ' ' && j > 0){
                space_count++;
            }else{
            ver_text[j++] = ' ';
            }

        }else if (isalpha(ch)){
            ver_text[j++] = ch;
        }
        else{
            continue;
        }
        
    }
    ver_text[j] = '\0'; 
    return space_count;
}


int main (){
    char text[] = " hello  world from  c  ";
    char ver_text [100];
    int space_delete = del_space(text, ver_text, sizeof(text));
    printf("%s \n", ver_text);
    printf("%d \n", space_delete);



    return 0;
}