#include <stdio.h>
#define MAX 100
typedef struct{
    int data[MAX];
    int top;
}Stack;
void init(Stack *s){
    s->top = -1;
}
int isEmpty(Stack *s){
    return s->top == -1;
}
void push(Stack *s, int val){
    s->data[++s->top] = val;
}
int pop(Stack *s){
    return s->data[s->top--];
}
int peek(Stack *s){
    return s->data[s->top];
}
void move(Stack *src, Stack *dest, char from, char to){
    int plate = pop(src);
    push(dest, plate);
    printf("移动盘子%d: %c → %c\n", plate, from, to);
}
int main(){
    Stack A,B,C;
    init(&A); init(&B); init(&C);
    int n;
    printf("请输入盘子数量n：");
    scanf("%d",&n);
    for(int i=n; i>=1; i--){
        push(&A, i);
    }
    if(n % 2 == 1){
        //奇数：A -> C
        while(!isEmpty(&A) || !isEmpty(&B)){
            move(&A, &C, 'A', 'C');
            if(isEmpty(&A) && isEmpty(&B)) break;

            if( !isEmpty(&A) && (isEmpty(&B) || peek(&A) < peek(&B)) )
                move(&A, &B, 'A', 'B');
            else
                move(&B, &A, 'B', 'A');
            if(isEmpty(&A) && isEmpty(&B)) break;

            if( !isEmpty(&B) && (isEmpty(&C) || peek(&B) < peek(&C)) )
                move(&B, &C, 'B', 'C');
            else
                move(&C, &B, 'C', 'B');
        }
    }else{
        //偶数：A -> B
        while(!isEmpty(&A) || !isEmpty(&B)){
            move(&A, &B, 'A', 'B');
            if(isEmpty(&A) && isEmpty(&C)) break;

            if( !isEmpty(&A) && (isEmpty(&C) || peek(&A) < peek(&C)) )
                move(&A, &C, 'A', 'C');
            else
                move(&C, &A, 'C', 'A');
            if(isEmpty(&A) && isEmpty(&C)) break;

            if( !isEmpty(&C) && (isEmpty(&B) || peek(&C) < peek(&B)) )
                move(&C, &B, 'C', 'B');
            else
                move(&B, &C, 'B', 'C');
        }
    }
    return 0;
}
