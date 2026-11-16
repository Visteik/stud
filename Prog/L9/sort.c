#include <stdio.h>
//Любой комментарий 2

void sort(int arr[3]){
    
        for (int i = 0; i < 2; i++){
            if (arr[i] > arr[i+1]){
                int t = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = t;
            }
    }
        for (int i = 0; i < 2; i++){
            if (arr[i] > arr[i+1]){
                int t = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = t;
            }
    }    
}


int main (){
    int a[3] = {4, 6};
    sort(a);
    for (int i =0; i < 3; i++){
        printf("%d ", a[i]);
    }
    printf("\n");


    return 0;
}