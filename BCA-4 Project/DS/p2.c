#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 100

char stack[MAX_SIZE][50];
int top = -1;

void push(char *word) {
    if (top >= MAX_SIZE - 1) {
        printf("-----You reached the limit, you can't add more words now!!------\n");
        return;
    }

    top++;
    strcpy(stack[top], word);

    return;
}

void pop() {
    if (top == -1) {
        printf("-----There is no value in document to undo.-----\n"); 
        return;
    } else {
        top--;
    }
}

void display() {
    if (top == -1) {
        printf("------The document is empty-----\n"); 
        return; 
    }
    for (int i = 0; i <= top; i++) {
        printf("%s ", stack[i]);
    }
    printf("\n");
}

int main() {
    char word[50];
    int choice;

    while (1) {
        printf("1. Add word\n");
        printf("2. Undo\n");
        printf("3. Display\n");
        printf("4. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter word: ");
                scanf("%49s", word); // here i Limited input to prevent buffer overflow, because the word length  is declared to 50 and last character should be null terminator.
                push(word);
                break;
            case 2:
                pop();
                break;
            case 3:
                display();
                break;
            case 4:
                return 0;
            default:
                printf("Invalid choice\n");
        }
    }
    return 0;
}