#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_ORDERS 100
#define MAX_ITEMS 100

struct Order {
    int id;
    char items[MAX_ITEMS];
    float price;
    int processed; 
}orders[MAX_ORDERS];

int orderCount = 0;

void addOrder() {
    if (orderCount < MAX_ORDERS)
    {
        printf("Enter Order ID: ");
        scanf("%d", &orders[orderCount].id);
        printf("Enter Items: ");
        scanf(" %[^\n]s", orders[orderCount].items);
        printf("Enter Price: ");
        scanf("%f", &orders[orderCount].price);
        orders[orderCount].processed = 0; 
        orderCount++;
        printf("Order added.\n");
    } 
    else
    {
        printf("Can't add more items!! limit out of bound\n");
    }
}

void processOrder() {
    if (orderCount > 0) 
    {
        for (int i = 0; i < orderCount; i++) 
        {
            if (orders[i].processed == 0) 
            {
                printf("Processing Order ID: %d\n", orders[i].id);
                printf("Items: %s\n", orders[i].items);
                printf("Price: %.2f\n", orders[i].price);
                orders[i].processed = 1;
                return;
            }
        }
        printf("No pending orders.\n");
    } 
    else
    {
        printf("No orders to process.\n");
    }
}

void displayOrders()
 {
    if (orderCount > 0)
     {
        printf("Pending Orders:\n");
        for (int i = 0; i < orderCount; i++) 
        {
            if (orders[i].processed == 0)
             {
                printf("ID: %d, Items: %s, Price: %.2f\n", orders[i].id, orders[i].items, orders[i].price);
            }
        }
    } 
    else 
    {
        printf("No orders.\n");
    }
}

void search() {
    int searchId;
    printf("Enter Order ID to search: ");
    scanf("%d", &searchId);
    for (int i = 0; i < orderCount; i++)
     {
        if (orders[i].id == searchId) 
        {
            if (orders[i].processed == 0) 
            {
                printf("Order found: ID: %d, Items: %s, Price: %.2f\n", orders[i].id, orders[i].items, orders[i].price);
            }
             else
            {
                printf("Order is processed.\n");
            }
            return;
        }
    }
    printf("Order not found.\n");
}

int main() {
    int choice;
    while (1) {
        printf("\n1. Add Order\n2. Process Order\n3. Display Orders\n4. Search Order\n5. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                addOrder();
                 break;
            case 2:
                processOrder();
                break;
            case 3: 
                displayOrders();
                break;
            case 4:
                search();
                break;
            case 5: 
                exit(0);
            default:   
                printf("Invalid choice.\n");
        }
    }
    return 0;
}