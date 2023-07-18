#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include "utils.h"

struct triangle
{
	int a;
	int b;
	int c;
};

typedef struct triangle triangle;


typedef struct triange_info_node {
    triangle tr;
    double area;
    struct triange_info_node* next;
} triange_info_node;

typedef struct triange_info_list {
    triange_info_node* head;
    int node_size;
    
} triange_info_list;

double calculate_area(const triangle* tr) {
    double p = (tr->a + tr->b + tr->c) / 2.0f;
    double inside_s = abs(p * (p-tr->a) * (p-tr->b) * (p-tr->c));
    double s = sqrt(inside_s);
    
    return s;
    
}

void insert_node(triange_info_list* tr_list, triangle tr, double area) {
    triange_info_node* new_node = (triange_info_node*) calloc(1, sizeof(triange_info_node));
    new_node->next = NULL;
    new_node->area = area;
    new_node->tr = tr;


    // insert head - list empty
    if(tr_list->head == NULL) {
        tr_list->head = new_node;
        tr_list->node_size++;
        return;
    }
    
    triange_info_node* temp = tr_list->head;
    triange_info_node* prev_node = temp;
    while (temp != NULL) {
        //find the correct location



        if (temp->area > area) {
            // insert head
            if(temp == prev_node) {
                new_node->next = temp;
                tr_list->head = new_node;
                tr_list->node_size++;
                return;
            }


            // insert the left of the node
            prev_node->next = new_node;
            new_node->next = temp;
            tr_list->node_size++;
            return;
        }

        prev_node = temp;
        temp = temp->next;

    }

    // insert tail
    prev_node->next = new_node;
    tr_list->node_size++;
}

void sort_by_area(triangle* tr, int n) {
	/**
	* Sort an array a of the length n
	*/
    
    // init list
    triange_info_list tr_list;
    tr_list.head = NULL;
    tr_list.node_size = 0;
    
    
    
    // calculate all areas
    for (int i = 0; i<n; ++i) {
        
        // insert it 
        double area = calculate_area(&tr[i]);
        triangle _tr = tr[i];
        
        insert_node(&tr_list, _tr, area);
        
    }

    triange_info_node* temp = tr_list.head;
    if (temp == NULL) {
        // list is empty and return
        return;
    }

    for (int i = 0; i<n; ++i) {
        tr[i] = temp->tr;
        
        temp = temp->next;
    }

    
}

int main()
{
	int n;
	scanf("%d", &n);
	triangle *tr = malloc(n * sizeof(triangle));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
	sort_by_area(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
	return 0;
}