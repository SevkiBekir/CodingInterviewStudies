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
    char *s = "Learning C is fun "; // for test
    // s = malloc(1024 * sizeof(char));
    // scanf("%[^\n]", s);
    // s = realloc(s, strlen(s) + 1);
    //Write your logic to print the tokens of the sentence here.
    
    int letter = -1;
    char word[1024] = {'\0'};
    int word_index = 0;
    while(s[++letter] != '\0'){
        if(s[letter] == ' ') {
            if (s[letter+1] == '\0'){
                break;
            }
            word[word_index] = '\0';
            printf("%s\n", word);
            word_index = 0;
            word[word_index] = '\0';
            continue;
        }
        
        word[word_index++] = s[letter];
    }

    //print last word
    word[word_index] = '\0';
    printf("%s\n", word);


    return 0;
}