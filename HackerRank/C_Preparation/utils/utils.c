#include "utils.h"


void print_begin_of_example(const char* title, int *ex_number){
    (*ex_number)++;

    printf("####### BEGIN OF Ex-%d ####### \n", *ex_number);
    printf("Title: %s\n", title);
}

void print_end_of_example(int ex_number){
    printf("####### END OF Ex-%d ####### \n", ex_number);
}

void print_end_of_file(){
    printf("####### END OF FILE ####### \n");
}

void print_array(int array[], int array_size){
    printf("Printing...\n");
    for(int i = 0; i < array_size; ++i){
        printf("array[%d]=%d\n", i, array[i]);
    }

    printf("Printing... - done\n");

}

void update_element_in_int_array(int array[], int array_size, int new_element, int index){
    printf("Updating...\n");
    printf("Old Element at %d index: %d\n", index, array[index]);
    array[index] = new_element;
    printf("Updating... - done\n");
    printf("New Element at %d index: %d\n", index, array[index]);
}

void update_element_in_float_array(float array[], int array_size, float new_element, int index){
    printf("Updating...\n");
    printf("Old Element at %d index: %f\n", index, array[index]);
    array[index] = new_element;
    printf("Updating... - done\n");
    printf("New Element at %d index: %f\n", index, array[index]);
}

void print_elem(int *array, int index){
    int *ptr = array+index;
    printf("Element value:%d\t address:%p\n", *ptr, ptr);
}

void init_array(int array[], int array_size){
    printf("Initializing...\n");
    
    for (int i = 0; i < array_size; i++){
        array[i] = 0;
    }

    printf("Initializing... - done\n");
}

void insert_tail(int array[], int array_size, int new_element){
    printf("Inserting...\n");
    
    int empty_index = -1;
    for (int i = 0; i < array_size; i++){
        if (array[i] == 0){
            empty_index = i;
            break;
        }
    }

    // not found any empty index yet
    if (empty_index == -1){
        printf("ERROR: Failed to find any empty index\n");
        return;
    }

    array[empty_index] = new_element;
    printf("Inserting at %d... - done\n", empty_index);
    
}

void delete_tail(int array[], int array_size){
    printf("Deleting...\n");
    int non_empty_index = 0;

    for (int i = array_size - 1; i >=0; i--){
        if (array[i] != 0){
            non_empty_index = i;
            break;
        }
    }

    array[non_empty_index] = 0;

    printf("Deleting... - done\n");
}


void check_file_open(FILE* file_ptr, const char* filename){
    if (file_ptr == NULL) {
        printf("Failed to open the file: %s\n", filename);
        exit(-1);
    }
}


void print_int(int variable){
    printf("Value: %d\n", variable);
}

void print_float(float variable){
    printf("Value: %f\n", variable);
}

void print_uint(unsigned int variable){
    printf("Value: %u\n", variable);
}

void print_int_ptr(int *variable_ptr){
    printf("Value: %d Address: %p\n", *variable_ptr, variable_ptr);
}

void free_int(int **variable_ptr){
    free(*variable_ptr);
    *variable_ptr=NULL;
}