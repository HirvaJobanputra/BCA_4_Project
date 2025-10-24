#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_ITEMS 100

struct inventory {
    int itemID;
    char itemName[100];
    float price;
    int quantity; 
};

struct inventory items[MAX_ITEMS];
int itemCount = 0; 

// Function to add a new item
void addItem() {
    if (itemCount < MAX_ITEMS) {
        printf("\nEnter item ID: ");
        scanf("%d", &items[itemCount].itemID);
        printf("Enter item name: ");
        scanf(" %[^\n]s", items[itemCount].itemName); // Improved input for names with spaces
        printf("Enter price: ");
        scanf("%f", &items[itemCount].price);
        printf("Enter quantity: ");
        scanf("%d", &items[itemCount].quantity);
        itemCount++;
        printf("Item added successfully!\n");
    } else {
        printf("Inventory is full. Cannot add more items.\n");
    }
}

// Function to remove an item
void removeItem() {
    int itemId;
    printf("\nEnter item ID to remove: ");
    scanf("%d", &itemId);

    for (int i = 0; i < itemCount; i++) {
        if (items[i].itemID == itemId) {
            // Shift remaining items to fill the gap
            for (int j = i; j < itemCount - 1; j++) {
                items[j] = items[j + 1];
            }
            itemCount--;
            printf("Item removed successfully!\n");
            return;
        }
    }

    printf("Item with ID %d not found.\n", itemId);
}

// Function to search for an item
void searchItem() {
    int itemId;
    printf("\nEnter item ID to search: ");
    scanf("%d", &itemId);

    for (int i = 0; i < itemCount; i++) {
        if (items[i].itemID == itemId) {
            printf("Item found:\n");
            printf("ID: %d\n", items[i].itemID);
            printf("Name: %s\n", items[i].itemName);
            printf("Price: %.2f\n", items[i].price);
            printf("Quantity: %d\n", items[i].quantity);
            return;
        }
    }

    printf("Item with ID %d not found.\n", itemId);
}

// Function to update item details
void updateItem() {
    int itemId;
    printf("\nEnter item ID to update: ");
    scanf("%d", &itemId);

    for (int i = 0; i < itemCount; i++) {
        if (items[i].itemID == itemId) {
            int choice;
            printf("What do you want to update?\n");
            printf("1. Price\n");
            printf("2. Quantity\n");
            scanf("%d", &choice);

            if (choice == 1) {
                printf("Enter new price: ");
                scanf("%f", &items[i].price);
            } else if (choice == 2) {
                printf("Enter new quantity: ");
                scanf("%d", &items[i].quantity);
            } else {
                printf("Invalid choice.\n");
            }
            printf("Item updated successfully!\n");
            return;
        }
    }

    printf("Item with ID %d not found.\n", itemId);
}

// Function to display all items
void displayItems() {
    if (itemCount == 0) {
        printf("Inventory is empty.\n");
        return;
    }

    printf("\nCurrent Inventory:\n");
    printf("------------------------------------------------------------------\n");
    printf("%-5s %-30s %-10s %-10s\n", "ID", "Name", "Price", "Quantity"); // Formatted output
    printf("------------------------------------------------------------------\n");

    for (int i = 0; i < itemCount; i++) {
        printf("%-5d %-30s %-10.2f %-10d\n", items[i].itemID, items[i].itemName, items[i].price, items[i].quantity);
    }
    printf("------------------------------------------------------------------\n");
}

int main() {
    int choice;

    printf("--------------------------------------------------\n");
    printf("Welcome to the Inventory Management System!\n");
    printf("--------------------------------------------------\n");

    while (1) {
        printf("\nChoose an operation:\n");
        printf("1. Add Item\n");
        printf("2. Remove Item\n");
        printf("3. Search Item\n");
        printf("4. Update Item\n");
        printf("5. Display Items\n");
        printf("6. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                addItem();
                break;
            case 2:
                removeItem();
                break;
            case 3:
                searchItem();
                break;
            case 4:
                updateItem();
                break;
            case 5:
                displayItems();
                break;
            case 6:
                printf("Exiting program.\n");
                return 0;
            default:
                printf("Invalid choice. Please try again.\n");
        }
    }

    return 0;
}