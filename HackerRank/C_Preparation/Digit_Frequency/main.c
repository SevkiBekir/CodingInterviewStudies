#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "utils.h"
#define DIGIT_SIZE 10

int main()
{
    char *s = "a11472o5t6"; // for test
    // char *s = malloc(1024 * sizeof(char));
    // scanf("%[^\n]", s);
    // s = realloc(s, strlen(s) + 1);
    int s_size = strlen(s);
    int digits[] = {0,0,0,0,0,0,0,0,0,0};
    
    for(int i = 0; i < s_size; ++i) {
        if (s[i] >= 48 || s[i] < 58) {
            char digit_ch = s[i];
            digits[digit_ch-48]++;
        }
    }
    
    for(int i = 0; i < DIGIT_SIZE; ++i) {
        printf("%d ", digits[i]);
    }
    
    

    return 0;
}