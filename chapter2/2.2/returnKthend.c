#include <stdio.h>
#include <stdlib.h>

typedef struct node{

   int val;
   struct node* next;

}node_t;


node_t* nthToLast(node_t* head, int k, int* i ){
    if (head == NULL){
        return NULL;
    }
    node_t* nd = nthToLast(head->next,k,i);
    *i= *i + 1;
    if(*i==k){
        return head;
    }
    return nd;
}

node_t* othernthToLast(node_t* head,int k){
    int i = 0;
    return nthToLast(head,k,&i);
}

void main(){

    int k = 2;
    //Create linked list
    node_t* head = NULL;
    node_t* current = NULL;
    node_t* kth = NULL;

    head = malloc(sizeof(node_t));// Should be error checked
    current = head;

    current->val = 0;
    current->next = malloc(sizeof(node_t));//Should be error checked
    current = current->next;

    current->val = 5;
    current->next = malloc(sizeof(node_t));//Should be error checked
    current = current->next;

    current->val = 2;
    current->next = malloc(sizeof(node_t));//Should be error checked
    current = current->next;

    current->val = 3;
    current->next = malloc(sizeof(node_t));//Should be error checked
    current = current->next;

    current->val = 9;
    current->next = malloc(sizeof(node_t));//Should be error checked
    current = current->next;

    kth = malloc(sizeof(node_t));

    kth = othernthToLast(head,k);
    printf("%d\n",kth->val);
}
