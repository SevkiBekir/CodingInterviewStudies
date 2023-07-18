

#ifndef UTILS_H
#define UTILS_H
#include <stdio.h>
#include <stdlib.h>

// DECLARATIONS

void print_begin_of_example(const char* title, int *ex_number);
void print_end_of_example(int ex_number);
void print_end_of_file();

void print_array(int array[], int array_size);
void update_element_in_int_array(int array[], int array_size, int new_element, int index);
void update_element_in_float_array(float array[], int array_size, float new_element, int index); // funcion overloading
void print_elem(int *array, int index);
void init_array(int array[], int array_size);
void insert_tail(int array[], int array_size, int new_element);
void delete_tail(int array[], int array_size);

void check_file_open(FILE* file_ptr, const char* filename);

void print_int(int variable);
void print_float(float variable);
void print_uint(unsigned int variable);
void print_int_ptr(int *variable_ptr);
void free_int(int **variable_ptr);

#endif //UTILS_H
