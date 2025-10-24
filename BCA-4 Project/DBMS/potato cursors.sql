DECLARE @RestaurantName VARCHAR(255);
DECLARE RestaurantCursor CURSOR FOR
SELECT RestaurantName FROM Restaurant;

OPEN RestaurantCursor;
FETCH NEXT FROM RestaurantCursor INTO @RestaurantName;

WHILE @@FETCH_STATUS = 0
BEGIN
    PRINT @RestaurantName;
    FETCH NEXT FROM RestaurantCursor INTO @RestaurantName;
END;

CLOSE RestaurantCursor;
DEALLOCATE RestaurantCursor;

---2nd
DECLARE @MenuId INT;
DECLARE MenuCursor CURSOR FOR
SELECT MenuId FROM Menu WHERE CuisineType = 'Italian';

OPEN MenuCursor;
FETCH NEXT FROM MenuCursor INTO @MenuId;

WHILE @@FETCH_STATUS = 0
BEGIN
    UPDATE Menu SET Price = Price * 1.10 WHERE MenuId = @MenuId; -- Increase price by 10%
    FETCH NEXT FROM MenuCursor INTO @MenuId;
END;

CLOSE MenuCursor;
DEALLOCATE MenuCursor;
---3rd
DECLARE @OrderId INT, @TotalAmount DECIMAL(10, 2);
DECLARE OrderCursor CURSOR FOR
SELECT OrderId, TotalAmount FROM Orders;

OPEN OrderCursor;
FETCH NEXT FROM OrderCursor INTO @OrderId, @TotalAmount;

WHILE @@FETCH_STATUS = 0
BEGIN
    IF @TotalAmount > 300
        PRINT 'Order ' + CAST(@OrderId AS VARCHAR(10)) + ' is above $300.';
    ELSE
        PRINT 'Order ' + CAST(@OrderId AS VARCHAR(10)) + ' is $300 or below.';
    FETCH NEXT FROM OrderCursor INTO @OrderId, @TotalAmount;
END;

CLOSE OrderCursor;
DEALLOCATE OrderCursor;
-- 4th
DECLARE @OrderId INT;
DECLARE OrderCursor CURSOR FOR
SELECT OrderId FROM Orders WHERE OrderStatus = 'Processing';

OPEN OrderCursor;
FETCH NEXT FROM OrderCursor INTO @OrderId;

WHILE @@FETCH_STATUS = 0
BEGIN
    UPDATE Orders SET OrderStatus = 'Completed' WHERE OrderId = @OrderId;
    FETCH NEXT FROM OrderCursor INTO @OrderId;
END;

CLOSE OrderCursor;
DEALLOCATE OrderCursor;
--5th
DECLARE @RestaurantId INT, @RestaurantName VARCHAR(255), @CuisineType VARCHAR(255);

DECLARE RestaurantCursor CURSOR FOR
SELECT RestaurantId, RestaurantName, CuisineType FROM Restaurant;

OPEN RestaurantCursor;
FETCH NEXT FROM RestaurantCursor INTO @RestaurantId, @RestaurantName, @CuisineType;

WHILE @@FETCH_STATUS = 0
BEGIN
    PRINT 'Restaurant ID: ' + CAST(@RestaurantId AS VARCHAR(10)) + ', Name: ' + @RestaurantName + ', Cuisine: ' + @CuisineType;
    FETCH NEXT FROM RestaurantCursor INTO @RestaurantId, @RestaurantName, @CuisineType;
END;

CLOSE RestaurantCursor;
DEALLOCATE RestaurantCursor;