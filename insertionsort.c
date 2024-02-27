#include <stdio.h>
#include <stdlib.h>

void insertionSort(int array[], int length) {
    for (int i = 1; i < length; i++) {
        int j = i - 1;
        int key = array[i];
        while (j >= 0 && array[j] > key) {
            array[j + 1] = array[j];
            j = j - 1;
        }
        array[j + 1] = key;
    }
}

int main() {
    int arr1[20];
    for (int i = 0; i < 20; i++) {
        arr1[i] = i + 1;
    }
    // Shuffle the array
    for (int i = 19; i > 0; i--) {
        int j = rand() % (i + 1);
        int temp = arr1[i];
        arr1[i] = arr1[j];
        arr1[j] = temp;
    }

    // Print the shuffled array
    printf("Shuffled array:\n");
    for (int i = 0; i < 20; i++) {
        printf("%d ", arr1[i]);
    }
    printf("\n");

    // Sort the array using insertion sort
    insertionSort(arr1, 20);

    // Print the sorted array
    printf("Sorted array:\n");
    for (int i = 0; i < 20; i++) {
        printf("%d ", arr1[i]);
    }
    printf("\n");

    return 0;
}

