#include <stdio.h>
#include <stdlib.h>
typedef struct PolyNode {
    int coef;//系数
    int exp;//指数
    struct PolyNode *next;
} PolyNode, *Polynomial;
// 创建多项式（输入 -1 -1 结束）
Polynomial CreatePoly() {
    Polynomial head = (Polynomial)malloc(sizeof(PolyNode));
    head->next = NULL;
    Polynomial p = head;
    int coef, exp;
    while (scanf("%d%d", &coef, &exp) && (coef != -1 || exp != -1)) {
        Polynomial newNode = (Polynomial)malloc(sizeof(PolyNode));
        newNode->coef = coef;
        newNode->exp = exp;
        newNode->next = NULL;
        p->next = newNode;
        p = newNode;
    }
    return head;
}
// 多项式相加
Polynomial AddPoly(Polynomial P1, Polynomial P2) {
    Polynomial head = (Polynomial)malloc(sizeof(PolyNode));
    head->next = NULL;
    Polynomial p = head, p1 = P1->next, p2 = P2->next;
    while (p1 && p2) {
        if (p1->exp == p2->exp) {
            int sum = p1->coef + p2->coef;
            if (sum != 0) {
                Polynomial newNode = (Polynomial)malloc(sizeof(PolyNode));
                newNode->coef = sum;
                newNode->exp = p1->exp;
                newNode->next = NULL;
                p->next = newNode;
                p = newNode;
            }
            p1 = p1->next;
            p2 = p2->next;
        }
        else if (p1->exp < p2->exp) {
            // 新建节点，不直接用原链表节点
            Polynomial newNode = (Polynomial)malloc(sizeof(PolyNode));
            newNode->coef = p1->coef;
            newNode->exp = p1->exp;
            newNode->next = NULL;
            p->next = newNode;
            p = newNode;
            p1 = p1->next;
        }
        else {
            // 新建节点，不直接用原链表节点
            Polynomial newNode = (Polynomial)malloc(sizeof(PolyNode));
            newNode->coef = p2->coef;
            newNode->exp = p2->exp;
            newNode->next = NULL;
            p->next = newNode;
            p = newNode;
            p2 = p2->next;
        }
    }
    // 剩余节点全部新建，绝不直接拼接
    while (p1) {
        Polynomial newNode = (Polynomial)malloc(sizeof(PolyNode));
        newNode->coef = p1->coef;
        newNode->exp = p1->exp;
        newNode->next = NULL;
        p->next = newNode;
        p = newNode;
        p1 = p1->next;
    }
    while (p2) {
        Polynomial newNode = (Polynomial)malloc(sizeof(PolyNode));
        newNode->coef = p2->coef;
        newNode->exp = p2->exp;
        newNode->next = NULL;
        p->next = newNode;
        p = newNode;
        p2 = p2->next;
    }
    return head;
}
// 打印多项式
void PrintPoly(Polynomial P) {
    Polynomial p = P->next;
    if (!p) {
        printf("0\n");
        return;
    }

    int first = 1;
    while (p) {
        if (!first) printf(" + ");
        first = 0;

        printf("%d", p->coef);
        if (p->exp > 0) {
            printf("x^%d", p->exp);
        }
        p = p->next;
    }
    printf("\n");
}
// 主函数
int main() {
    Polynomial P1 = CreatePoly();
    Polynomial P2 = CreatePoly();
    Polynomial P3 = AddPoly(P1, P2);
    printf("first1:");
    PrintPoly(P1);
    printf("second2:");
    PrintPoly(P2);
    printf("total:");
    PrintPoly(P3);
    return 0;
}