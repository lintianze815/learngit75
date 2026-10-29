#define UNICODE
#define _UNICODE
#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define MAX_STACK 100
#define TOKEN_LEN 20
// 运算符栈
typedef struct {
    char data[MAX_STACK];
    int top;
} OpStack;
// 操作数栈
typedef struct {
    double data[MAX_STACK];
    int top;
} NumStack;
HWND hEditBox;
WCHAR inputBuf[256] = { 0 };
// 按钮配置
const WCHAR* btnTexts[] = {
    L"C", L"←", L"/", L"*",
    L"7", L"8", L"9", L"-",
    L"4", L"5", L"6", L"+",
    L"1", L"2", L"3", L"=",
    L"0", L"."
};
const unsigned int btnTotal = sizeof(btnTexts) / sizeof(btnTexts[0]);
int btnX[] = { 10,70,130,190, 10,70,130,190, 10,70,130,190, 10,70,130,190, 10,70 };
int btnY[] = { 80,80,80,80,    130,130,130,130, 180,180,180,180, 230,230,230,230, 280,280 };
int btnW[] = { 50,50,50,50,    50,50,50,50,    50,50,50,50,    50,50,50,50,    80,50 };
// 栈操作
void InitOpStack(OpStack* s) { s->top = -1; }
void InitNumStack(NumStack* s) { s->top = -1; }
int IsOpEmpty(OpStack* s) { return s->top == -1; }
int IsNumEmpty(NumStack* s) { return s->top == -1; }
void PushOp(OpStack* s, char c) { if (s->top < MAX_STACK - 1) s->data[++s->top] = c; }
void PushNum(NumStack* s, double num) { if (s->top < MAX_STACK - 1) s->data[++s->top] = num; }
int PopOp(OpStack* s, char* out) { if (IsOpEmpty(s)) return 0; *out = s->data[s->top--]; return 1; }
int PopNum(NumStack* s, double* out) { if (IsNumEmpty(s)) return 0; *out = s->data[s->top--]; return 1; }
// 运算符优先级
int GetOpPri(char op) {
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    return 0;
}
// 判断是否为四则运算符
int IsOperator(WCHAR c)
{
    return c == L'+' || c == L'-' || c == L'*' || c == L'/';
}

// 中缀转后缀
void InfixToSuffix(char* infix, char suffix[][TOKEN_LEN], int* suffixLen) {
    OpStack opSt;
    InitOpStack(&opSt);
    *suffixLen = 0;
    char numBuf[TOKEN_LEN] = { 0 };
    int bufIdx = 0;

    for (int i = 0; infix[i] != '\0'; i++) {
        char c = infix[i];
        if ((c >= '0' && c <= '9') || c == '.') {
            if (bufIdx < TOKEN_LEN - 1)
                numBuf[bufIdx++] = c;
        }
        else {
            if (bufIdx > 0) {
                strcpy(suffix[(*suffixLen)++], numBuf);
                memset(numBuf, 0, TOKEN_LEN);
                bufIdx = 0;
            }
            while (!IsOpEmpty(&opSt) && GetOpPri(opSt.data[opSt.top]) >= GetOpPri(c)) {
                char topOp;
                PopOp(&opSt, &topOp);
                sprintf(suffix[(*suffixLen)++], "%c", topOp);
            }
            PushOp(&opSt, c);
        }
    }
    if (bufIdx > 0)
        strcpy(suffix[(*suffixLen)++], numBuf);

    while (!IsOpEmpty(&opSt)) {
        char topOp;
        PopOp(&opSt, &topOp);
        sprintf(suffix[(*suffixLen)++], "%c", topOp);
    }
}

// 后缀表达式计算
double CalcSuffix(char suffix[][TOKEN_LEN], int suffixLen, int* errCode) {
    *errCode = 0;
    NumStack numSt;
    InitNumStack(&numSt);

    for (int i = 0; i < suffixLen; i++) {
        char token[TOKEN_LEN];
        strncpy(token, suffix[i], TOKEN_LEN - 1);
        token[TOKEN_LEN - 1] = '\0';

        if (token[0] == '+' || token[0] == '-' || token[0] == '*' || token[0] == '/') {
            double a, b, res;
            if (!PopNum(&numSt, &b) || !PopNum(&numSt, &a)) {
                *errCode = 1;
                return 0;
            }
            switch (token[0]) {
                case '+': res = a + b; break;
                case '-': res = a - b; break;
                case '*': res = a * b; break;
                case '/':
                    if (fabs(b) < 1e-9) {
                        *errCode = 2;
                        return 0;
                    }
                    res = a / b;
                    break;
                default:
                    *errCode = 1;
                    return 0;
            }
            PushNum(&numSt, res);
        }
        else {
            PushNum(&numSt, atof(token));
        }
    }

    double ans = 0;
    if (!PopNum(&numSt, &ans))
        *errCode = 1;
    return ans;
}

// 窗口过程
LRESULT CALLBACK CalcWndProc(HWND hWnd, UINT msg, WPARAM wParam, LPARAM lParam) {
    switch (msg)
    {
    case WM_CREATE:
    {
        LPCREATESTRUCTW createInfo = (LPCREATESTRUCTW)lParam;
        // 编辑框
        hEditBox = CreateWindowW(L"EDIT", L"0",
            WS_CHILD | WS_VISIBLE | ES_READONLY | ES_RIGHT,
            10, 10, 270, 60, hWnd, (HMENU)1001, createInfo->hInstance, NULL);
        // 创建按钮
        for (unsigned int i = 0; i < btnTotal; i++)
        {
            CreateWindowW(L"BUTTON", btnTexts[i],
                WS_CHILD | WS_VISIBLE,
                btnX[i], btnY[i], btnW[i], 40,
                hWnd, (HMENU)i, createInfo->hInstance, NULL);
        }
        break;
    }
    case WM_COMMAND:
    {
        int btnId = LOWORD(wParam);
        if (btnId < 0 || (unsigned int)btnId >= btnTotal) break;
        const WCHAR* btnText = btnTexts[btnId];
        WCHAR key = btnText[0];
        size_t curLen = wcslen(inputBuf);

        // 清空 C
        if (!wcscmp(btnText, L"C"))
        {
            memset(inputBuf, 0, sizeof(inputBuf));
            SetWindowTextW(hEditBox, L"0");
            break;
        }
        // 退格 ←
        else if (!wcscmp(btnText, L"←"))
        {
            if (curLen > 0)
            {
                curLen--;
                inputBuf[curLen] = L'\0';
            }
            SetWindowTextW(hEditBox, curLen > 0 ? inputBuf : L"0");
            break;
        }
        // 计算 =
        else if (!wcscmp(btnText, L"="))
        {
            if (curLen == 0)
            {
                SetWindowTextW(hEditBox, L"输入不能为空");
                break;
            }
            WCHAR lastCh = inputBuf[curLen - 1];
            // 末尾不能是运算符或单独小数点
            if (IsOperator(lastCh) || lastCh == L'.')
            {
                SetWindowTextW(hEditBox, L"表达式格式错误");
                break;
            }

            char infixAnsi[256] = { 0 };
            WideCharToMultiByte(CP_ACP, 0, inputBuf, (int)curLen, infixAnsi, 255, NULL, NULL);
            char suffixArr[MAX_STACK][TOKEN_LEN] = { 0 };
            int sufLen, err;
            InfixToSuffix(infixAnsi, suffixArr, &sufLen);
            double result = CalcSuffix(suffixArr, sufLen, &err);

            if (err == 1)
                SetWindowTextW(hEditBox, L"表达式格式错误");
            else if (err == 2)
                SetWindowTextW(hEditBox, L"除数不能为0");
            else
            {
               WCHAR resStr[50];
               const size_t resStrMaxLen = sizeof(resStr) / sizeof(resStr[0]) - 1;
                snwprintf(resStr, resStrMaxLen, L"%g", result);
                memset(inputBuf, 0, sizeof(inputBuf));
                wcscpy(inputBuf, resStr);
                SetWindowTextW(hEditBox, resStr);
            }
            break;
        }
        // 数字、运算符、小数点
        else
        {
            if (curLen >= 250) break;

            // 1. 允许开头 / 运算符后输入负号
            if (key == L'-')
            {
                if (curLen == 0 || IsOperator(inputBuf[curLen - 1]))
                {
                    wcscat(inputBuf, btnText);
                    SetWindowTextW(hEditBox, inputBuf);
                    break;
                }
            }

            // 2. 禁止连续运算符
            if (IsOperator(key) && curLen > 0 && IsOperator(inputBuf[curLen - 1]))
                break;

            // 3. 小数点：当前数字段只能一个小数点
            if (key == L'.')
            {
                int hasDot = 0;
                for (int i = (int)curLen - 1; i >= 0; i--)
                {
                    if (inputBuf[i] == L'.') { hasDot = 1; break; }
                    if (IsOperator(inputBuf[i])) break;
                }
                if (hasDot) break;
            }

            wcscat(inputBuf, btnText);
            SetWindowTextW(hEditBox, inputBuf);
            break;
        }
        break;
    }
    case WM_CLOSE:
        DestroyWindow(hWnd);
        break;
    case WM_DESTROY:
        PostQuitMessage(0);
        break;
    default:
        return DefWindowProcW(hWnd, msg, wParam, lParam);
    }
    return 0;
}
// 入口函数
int WINAPI WinMain(HINSTANCE hInst, HINSTANCE hPrev, LPSTR lpCmd, int nShow) {
    (void)hPrev;
    (void)lpCmd;
    WNDCLASSEXW winClass = { 0 };
    winClass.cbSize = sizeof(WNDCLASSEXW);
    winClass.lpfnWndProc = CalcWndProc;
    winClass.hInstance = hInst;
    winClass.lpszClassName = L"StackCalcClass";
    winClass.hbrBackground = (HBRUSH)(COLOR_WINDOW + 1);
    RegisterClassExW(&winClass);
    HWND hMainWnd = CreateWindowExW(0, L"StackCalcClass", L"栈实现计算器",
        WS_OVERLAPPED | WS_CAPTION | WS_SYSMENU,
        100, 100, 300, 360, NULL, NULL, hInst, NULL);
    ShowWindow(hMainWnd, nShow);
    UpdateWindow(hMainWnd);
    MSG msg;
    while (GetMessageW(&msg, NULL, 0, 0) > 0)
    {
        TranslateMessage(&msg);
        DispatchMessageW(&msg);
    }
    return (int)msg.wParam;
}