#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include "utils.h"

void reverse_number(int number) {
    int reversed_number = 0;

    int temp = number;
    int reminder = 0;
    while(temp > 0) {
        reminder = temp % 10;
        reversed_number = reversed_number * 10 + reminder;
        temp /= 10;
    }

    printf("The reversed number of %d: %d\n", number, reversed_number);
}

int main()
{
    reverse_number(321);
	
	return 0;
}