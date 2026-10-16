#include<stdio.h>
#define MAX 5

int deque[MAX];
int front = -1,rear =-1;

void insertFront(int x){
    if((front == 0 && rear ==MAX -1)|| front == rear +1){
        printf("Deque Overflow\n");
        return;
    }
}