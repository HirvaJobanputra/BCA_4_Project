#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 100
struct Order 
{
    int itemId;
    char itemName[100];
    int processed; 
    float price;
};
struct Order items[MAX];
int front = -1;
int rear = -1;
int nextOrderId = 1; // Start order IDs from 1

void addOrder(struct Order order) {
    if (rear == MAX - 1) 
    {
        printf("Order list is full!1, can not add more orders.\n");
    } 
    else 
    {
        if (front == -1) 
        {
            front = 0;
        }
        rear++;
        items[rear] = order;
        printf("Order %d \"%s\" added to queue\n", order.itemId, order.itemName);
    }
}

void process()
{
    if (front == -1 || front > rear) 
    {
        printf("Queue Underflow (No orders to process)\n");
    }
    else
    {
        printf("Processing Order %d (%s)\n", items[front].itemId, items[front].itemName);
        items[front].processed = 1; 
        front++;
        if (front > rear) 
        {
            front = -1;
            rear = -1; 
        }
    }
}

void display() 
{
    if (front == -1) 
    {
        printf("No pending orders\n");
    }
    else 
    {
        printf("Pending Orders:\n");
        for (int i = front; i <= rear; i++) 
        {
            printf("Order ID: %d | Item: %s | Price: %.2f | Processed: %d\n", items[i].itemId, items[i].itemName, items[i].price, items[i].processed);
        }
        printf("\n");
    }
}
void search(int orderId)
{
    if (front == -1)
    {
        printf("Queue is empty. Order %d not found.\n", orderId);
        return;
    }
    for (int i = front; i <= rear; i++)
    {
        if (items[i].itemId == orderId) 
        {
            printf("Order %d (%s) found in queue. Price: %.2f, Processed: %s\n", items[i].itemId, items[i].itemName, items[i].price, items[i].processed ? "Yes" : "No");
            return;
        }
    }
    printf("Order %d not found in queue.\n", orderId);
}
int main() {
    int choice, orderId;
    struct Order newOrder;
    while (1) {
        printf("\n1. Add Order\n");
        printf("2. Process Order\n");
        printf("3. Display Orders\n");
        printf("4. Search Order\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                newOrder.itemId = nextOrderId++; // Generate and assign Order ID
                printf("Enter Item Name: ");
                scanf(" %[^\n]s", newOrder.itemName); 
                printf("Enter Price: ");
                scanf("%f", &newOrder.price);
                newOrder.processed = 0; 
                addOrder(newOrder);
                break;
            case 2:
                process();
                break;
            case 3:
                display();
                break;
            case 4:
                printf("Enter Order ID to search: ");
                scanf("%d", &orderId);
                search(orderId);
                break;
            case 5:
                exit(0);
            default:
                printf("Invalid choice\n");
        }
    }
    return 0;
}