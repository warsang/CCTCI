#include <stdio.h>
#include <stdlib.h>

typedef struct node { 

    int val;
    struct node* next;

} node_t;

typedef struct linked_list{
    node_t* head;
} llist_t;


void *errorchecked_malloc(unsigned int size){
    //An error checked malloc from Hacking the art of exploitation
    void *ptr;
    ptr = malloc(size);
    if(ptr == NULL){
        fprintf(stderr, "Error could not allocate heap memory.\n");
        exit(-1);
    }
}

llist_t create_linked_list(int number_of_nodes){
    //Creates a linked list with default value of 0
    llist_t linked_list;
    node_t* head = NULL;
    node_t* current = NULL;

    int i;

    head =(node_t*) errorchecked_malloc(sizeof(node_t));
    linked_list.head = head;
    current = linked_list.head;
    
    for(i=1;i<= number_of_nodes;i++){
    
        current->val = 0;
        current->next = (node_t*) errorchecked_malloc(sizeof(node_t));
        current = current->next;
    
    }

    return linked_list;
}

void print_list(llist_t linked_list){
    node_t* current = linked_list.head;

    while(current != NULL){
        printf("%d\n",current->val);
        current = current->next;
    }
}

void apend(llist_t linked_list,int val){

    node_t* current = linked_list.head;
    while(current-> next != NULL){
        current = current->next;
    }

    current->next = (node_t*) errorchecked_malloc(sizeof(node_t));
    current->next->val = val;
    current->next->next = NULL;

}

void pop(llist_t* linked_list){
    int retval=-1;
    node_t* next_node = NULL;

    if(linked_list->head == NULL){
        exit(-1);
    }

    next_node = linked_list->head->next;
    retval = linked_list->head->val;
    free(linked_list->head);
    linked_list->head = next_node;

}

void prepend(llist_t* linked_list, int val){

    node_t* current = linked_list->head;
    node_t* new_head = (node_t*) errorchecked_malloc(sizeof(node_t));

    new_head->val = val;
    new_head->next = linked_list->head;
    linked_list->head = new_head;

}

void remove_last(llist_t* linked_list){

    int retval = 0;
    
    //Optimisation => Only one item in list, remove it
    if(linked_list->head == NULL){
        retval = linked_list->head->val;
        free(linked_list->head);
    }
    
    //Go to last node
    node_t* current = linked_list->head;
    while(current->next->next !=NULL){
        current = current->next;
    }

    retval = current->next->val;
    free(current->next);
    current->next = NULL;
}

int remove_by_value(llist_t* linked_list,int value){

   node_t* current = linked_list->head;
   node_t* stock_node = NULL;
    //itterate through list
   while(current->next->next != NULL){
   
       if(current->next->val==value){
           //delete the value
           stock_node = current->next->next;
           free(current->next);
           current->next = stock_node;
           return 0;
       }
   }
   return 1;
}

int main(){
    
    llist_t linked_list;
    linked_list = create_linked_list(10);
    printf("Created linked list\n");
    print_list(linked_list);
    apend(linked_list,8);
    prepend(&linked_list,9);
    prepend(&linked_list,12);
    printf("Added elements\n");
    print_list(linked_list);
    pop(&linked_list);
    printf("popping an elemnt\n");
    print_list(linked_list);
    printf("Removing last element\n");
    remove_last(&linked_list);
    print_list(linked_list);
    apend(linked_list,17);
    apend(linked_list,12);
    printf("Remove by value");
    remove_by_value(&linked_list,17);
    print_list(linked_list);
    return 0;

}

