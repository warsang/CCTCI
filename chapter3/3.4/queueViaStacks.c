#include <stdio.h>
#include <stdlib.h>

//TODO: Not yet implemented
typedef struct stack{

    int* values;

}stack;

typedef struct queue{

    stack first_stack;
    stack second_stack;
    
}queue;

void stack_push(stack* stackTarget, int newValue){
   

}

void main(){

    int table[11] = {1,4,2,6,3,5,9,19,2,3};
    stack* first_stack = NULL;
    stack* second_stack = NULL;
    queue* my_queue = NULL;

    first_stack = malloc(sizeof(stack));
    second_stack = malloc(sizeof(stack));
    my_queue = malloc(sizeof(queue));

}
