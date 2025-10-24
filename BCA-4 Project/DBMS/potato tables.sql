-- Restaurant Table
CREATE TABLE Restaurant (
    RestaurantId INT PRIMARY KEY IDENTITY(1,1),
    RestaurantName VARCHAR(255) NOT NULL,
    CuisineType VARCHAR(255),
    Address TEXT,
    PhoneNumber VARCHAR(20),
    Rating DECIMAL(2,1)
);

-- Orders Table
CREATE TABLE Orders (
    OrderId INT PRIMARY KEY IDENTITY(1,1),
    UserId INT FOREIGN KEY REFERENCES Users(UserId), -- Assuming Users table exists (from second image)
    RestaurantId INT FOREIGN KEY REFERENCES Restaurant(RestaurantId),
    OrderDate DATETIME DEFAULT GETDATE(),
    TotalAmount DECIMAL(7,2),
    OrderStatus VARCHAR(50) DEFAULT 'Pending'
);

-- OrderItems Table
CREATE TABLE OrderItems (
    OrderItemId INT PRIMARY KEY IDENTITY(1,1),
    OrderId INT FOREIGN KEY REFERENCES Orders(OrderId),
    MenuId INT FOREIGN KEY REFERENCES Menu(MenuId),
    Quantity INT NOT NULL,
    Price DECIMAL(5,2) NOT NULL
);

-- Menu Table
CREATE TABLE Menu (
    MenuId INT PRIMARY KEY IDENTITY(1,1),
    RestId INT FOREIGN KEY REFERENCES Restaurant(RestaurantId), -- Assuming Restaurant table exists (from first image)
    ItemName VARCHAR(255) NOT NULL,
    Description TEXT,
    Price DECIMAL(5,2) NOT NULL,
    Availability BIT DEFAULT 1 -- Boolean in MS SQL is BIT
);

-- Users Table
CREATE TABLE Users (
    UserId INT PRIMARY KEY IDENTITY(1,1),
    Username VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) UNIQUE NOT NULL,
    Address TEXT NOT NULL,
    Password VARCHAR(255) NOT NULL
);

-- DeliveryStaff Table
CREATE TABLE DeliveryStaff (
    DeliveryStaffId INT PRIMARY KEY IDENTITY(1,1),
    StaffName VARCHAR(255) NOT NULL,
    PhoneNumber VARCHAR(20) UNIQUE NOT NULL,
    VehicleType VARCHAR(50)
);