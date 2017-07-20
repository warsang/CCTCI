#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Time complexity
//O(len(str1) +len(str2)) as len(str1) is equivalent to len(str2) (close values) O(len(str1)) => O(n)
//Memory complexity
//same reasoning

int insert(char* string1,char* string2){
    int i = 0;
    int j = 0;
    int insert_counter = 0;
    while(i <= (strlen(string1) -1) | j <= (strlen(string2) -1)){
        if(j = strlen(string2)){
            insert_counter += 1;
            break;
        }
        if(string1[i] == string2[j]){
            i += 1;
            j += 1;
        }
        else{
            insert_counter += 1;
            i += 1;
        }
    }
    return insert_counter;
}

int oneAway(char* string1, char* string2){

    int length1 = strlen(string1);
    int length2 = strlen(string2);
    int differences = 0;
    int i;
    if(length1 != length2 && length1 != (length2 +1) && length1 != (length2 -1)){
        return 0;
    }
    //Case1: replace
    if(length1 == length2){
        for(i = 0; i <= (length1 -1); i++){
            if(string1[i] != string2[i]){
                differences += 1;
            }
        }
    }   
    //Case2: Insert in 2
    else if(length1 == (length2 + 1)){
        differences = insert(string1,string2);
    }
    //Case3
    else{
        differences = insert(string2,string1);
    }
    if(differences > 1){
        return 0;
    }
    else{
        return 1;
    }

}

void main(){

    printf("%d\n",oneAway("pale","ple"));
    printf("%d\n",oneAway("pales","pale"));
    printf("%d\n",oneAway("pale","bale"));
    printf("%d\n",oneAway("pale","bake"));

}

