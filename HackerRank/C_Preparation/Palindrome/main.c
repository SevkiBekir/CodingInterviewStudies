#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include "utils.h"

void check_palindrome(const char* str) {
    int start = 0;
    int end = strlen(str) - 1;

    while(end > start) {
        if(str[start++] != str[end--]) {
            printf("%s : It's NOT palindrome\n", str);
            return;
        }
    }

    printf("%s : It's palindrome :) \n", str);

}

int main()
{
	check_palindrome("acca");
	check_palindrome("acdca");
	check_palindrome("acdcca");
	return 0;
}