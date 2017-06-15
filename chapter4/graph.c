#include <stdio.h>
#include <stdlib.h>

#define CHILDREN 2
#define NODES 10

typedef struct Node{
    
    char* name;
    struct Node* children[2];

}Node;

typedef struct Graph{

    struct Node* nodes[NODES];

}Graph;

int adjacency_matrix[NODES][NODES]={0};


void main(){

    Node* node1 = malloc(sizeof(Node));
    Node* node2 = malloc(sizeof(Node));
    Node* node3 = malloc(sizeof(Node));

    Graph* graph = malloc(sizeof(Graph));
    graph->nodes[0]=node1;
    graph->nodes[1]=node2;
    graph->nodes[2]=node3;

    adjacency_matrix[0][1]=1;
    adjacency_matrix[1][2]=1;
    adjacency_matrix[2][1]=1;
    adjacency_matrix[0][2]=1;

}
