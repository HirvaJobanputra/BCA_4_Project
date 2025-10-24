----------1st

CREATE FUNCTION GetItemName (
    @MenuId INT
)
RETURNS VARCHAR(255)
AS
BEGIN
	deCLARE @ItemName VARCHAR(255);
    SELECT @ItemName = ItemName
    FROM Menu
    WHERE MenuId = @MenuId;
    rETURN @ItemName;
END;
SELECT dbo.GetItemname(5); 

------------2nd
CREATE FUNCTION GetRestaurantName (
    @RestaurantId INT
)
RETuRNS VARCHAR(255)
AS
BEGIN
    DEClARE @RestaurantName VARCHAR(255);
    SELECT @RestaurantName = RestaurantName
    FROM Restaurant
    WHERE RestaurantId = @RestaurantId;
    rETURN @RestaurantName;
EnD;
SELECT dbo.GetRestaurantName(3); 

--------3rd
CREATE FUNCTION GetOrderStatusDescription (
    @OrderStatus VARCHAR(50)
)
RETURNS VARCHAR(100)
AS
BEGIN
    DECLARE @Description VARCHAR(100);
    -- You can add more complex logic here to map status codes to descriptions
    IF @OrderStatus = 'Pending'
        SET @Description = 'Order has been placed but not yet processed.';
    ELSE IF @OrderStatus = 'Out for Delivery'
        SET @Description = 'Order is on its way.';
    ELSE IF @OrderStatus = 'Delivered'
        SET @Description = 'Order has been delivered.';
    ELSE
        SET @Description = 'Unknown Status';
    RETURN @Description;
END;

SELECT dbo.GetOrderStatusDescription('Out for Delivery');
-----------4th
CREATE FUNCTION GetUserOrders (
    @UserId INT
)
RETURNS TABLE
AS
RETURN (
    SELECT OrderId, OrderDate, TotalAmount, OrderStatus
    FROM Orders
    WHERE UserId = @UserId
);

SELECT * FROM dbo.GetUserOrders(1); 
-------------5th
CREATE FUNCTION GetRestaurantMenuItems (
    @RestaurantId INT
)
RETURNS TABLE
AS
RETURN (
    SELECT MenuId, ItemName, Price
    FROM Menu
    WHERE RestId = @RestaurantId
);
SELECT * FROM dbo.GetRestaurantMenuItems(3); 