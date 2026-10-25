#include<stdio.h>
int* reverse_el(int new_arr[], int new_size){
    int slow = 0;
    for (int fast = new_size - 1; fast >= 0; fast--){
        new_arr[slow] = new_arr[fast];
        slow++;
    }
    return new_arr;
}

int main() {
    int arr[] = {1, 2, 2, 3, 3, 1, 1, 5, 6, 7};
    int size = sizeof(arr)/sizeof(arr[0]);
    printf("Исходный масив: \n");
    for (int i = 0; i < size; i++){
        printf(" %d", arr[i]);
    }
    int* rev[] = reverse_el(arr, size);
    for (int i = 0; i < size; i++){
        printf(" %d", rev[i]);
    }
    return 0;
}