#include <stdio.h>
#include <stdlib.h>


//Time complexity:
// deleteNode function Depends where the deleted node is located as we itterate up until the deleted node but roughly O(n) where n is the size of the linked list
// main itterates the llist array which is the size of the linked list (imagine this was a for loop) and the linked list itself to print it. Because it itterates through the whole list -1 element we can consider it to be O(n)
// So complexity is O(n + n + (n-1)) = O(3n) = O(n)
//Size complexity: 
// O(n + n-1 + n*sizeofNode) (two arrays of size n and n-1  as well as n times the allocated size of node) => O(n)

typedef struct node{

    char* name;
    struct node* child;
}node;


void deleteNode(node* anode ){

    anode->name = anode->child->name;
    anode->child = anode->child->child;
    
}



void main(){

    node* llist [6];
    
    node* a_node = malloc(sizeof(node));
    node* f = malloc(sizeof(node));
    node* e = malloc(sizeof(node));
    node* d = malloc(sizeof(node));
    node* c = malloc(sizeof(node));
    node* b = malloc(sizeof(node));
    node* a = malloc(sizeof(node));

    f->name = "f";
    f->child = 0;
    e->name = "e";
    e->child = f;
    d->name = "d";
    d->child = e;
    c->name = "c";
    c->child = d;
    b->name = "b";
    b->child = c;
    a->name = "a";
    a->child = b;

    llist[0] = a;
    llist[1] = b;
    llist[2] = c;
    llist[3] = d;
    llist[4] = e;
    llist[5] = f;

    deleteNode(c);
    free(d);

    a_node = a;

    while(1){
        if(a_node->child == 0){
            printf("%s",a_node->name);
            break;
        }
        else{
            printf("%s ->", a_node->name);
            a_node = a_node->child;
        }
    }
}
