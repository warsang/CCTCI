#include <stdio.h>
#include <stdlib.h>
#define MAXSIZE 5

typedef struct stack
{
    int stk[MAXSIZE];
    int top;
}stack_t;

int push(stack_t* s,int num)
{
    if(s->top == (MAXSIZE -1)){
        printf("Stack is Full\n");
        return -1;
    }
    else{
        s->top = s->top + 1;
        s->stk[s->top]=num;
    }
    return 0;
}

int pop(stack_t* s){
    
    int num;
    if(s->top == -1){
        printf("Stack is Empty\n");
        return(s->top);
    }
    else{
        num =s->stk[s->top];
        printf("Popped element is =%d \n",s->stk[s->top]);
        s->top = s->top -1;
    }
    return(num);
}

void display(stack_t* s){
    int i;
    if(s->top == -1){
        printf("Stack is empty \n");
        return;
    }
    else
    {
       for(i=s->top;i>=0;i--){
           printf("%d\n",s->stk[i]);
       }
    }
    printf("\n");
}

int main(){

    stack_t*  stack_test;
    stack_test = malloc(sizeof(stack_t));
    push(stack_test,8);
    push(stack_test,12);
    push(stack_test,9);
    push(stack_test,10);
    display(stack_test);
    pop(stack_test);
    display(stack_test);
    free(stack_test);
     
}
