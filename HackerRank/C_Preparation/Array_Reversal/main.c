#include <stdio.h>
#include <stdlib.h>

#include "utils.h"

void swap(int*a, int*b) {
    printf("swapping\n");

    int temp = *a;
    *a = *b;
    *b = temp;
}

int main()
{
    int num, *arr, i;
    scanf("%d", &num);
    arr = (int*) malloc(num * sizeof(int));
    for(i = 0; i < num; i++) {
        scanf("%d", arr + i);
    }

    printf("array done\n");
    print_array(arr, num);
    /* Write the logic to reverse the array. */
    int first_half = 0;
    int second_half = num - 1;

    
    while(first_half != second_half) {
        swap(arr+first_half, arr+second_half);
        print_int(first_half);
        print_int(second_half);
    
        first_half++;
        second_half--;

        if (first_half - 1 == second_half) {
            break;
        }

    }
    
    printf("swap done\n");
    print_array(arr, num);
    

    for(i = 0; i < num; i++)
        printf("%d ", *(arr + i));
    return 0;
}