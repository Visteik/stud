#include<stdio.h>

int main(){
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8};
    int size = sizeof(arr)/sizeof(arr[0]);
    int max = arr[0];
    int indx = 0;
    for (int i = 0; i < size; i++){
        if (arr[i] > max){
            max = arr[i];
            indx = i;
        }
    } 
    printf("Максимально знанчение = %d, индекс = %d\n", max, indx);





return 0;
}