-------------1st Trigger  

CREATE TRIGGER UpdateRestaurantRating
ON Orders
AFTER INSERT
AS
BEGIN
   
    UPDATE Restaurant
    SET Rating = (
        SELECT AVG(TotalAmount)
        FROM Orders
        WHERE RestaurantId = (SELECT RestaurantId FROM inserted)
    )
    WHERE RestaurantId = (SELECT RestaurantId FROM inserted);
END;
-------------2nd Trigger
CREATE TRIGGER log_user_update
ON users
AFTER UPDATE
AS
BEGIN
    DECLARE @old_username VARCHAR(255);
    DECLARE @new_username VARCHAR(255);
    SELECT @old_username = username FROM DELETED;
    SELECT @new_username = username FROM INSERTED;
    INSERT INTO user_log (old_username, new_username, action, log_time) -- Assuming user_log table has old_username
    VALUES (@old_username, @new_username, 'UPDATED', GETDATE());
END;
-------------3rd Trigger
CREATE TRIGGER OrderDeletedMessage
ON Orders
AFTER DELETE
AS
BEGIN
    DECLARE @OrderId INT;
    SELECT @OrderId = OrderId FROM deleted;

    PRINT 'Order with ID: ' + CAST(@OrderId AS VARCHAR(10)) + ' has been deleted.';
END;
-------------4th Trigger
CREATE TRIGGER ControlUserInsertion
ON Users
INSTEAD OF INSERT
AS
BEGIN
    IF (SELECT LEN(Username) FROM inserted) > 5 -- Example: Check Username length
    BEGIN
        INSERT INTO Users (Username, Email, Phone, Address, Password)
        SELECT Username, Email, Phone, Address, Password FROM inserted;
        PRINT 'New user added.';
    END
    ELSE
    BEGIN
        PRINT 'Username is too short. User not added.';
    END;
END;
-------------5th Trigger
CREATE TRIGGER LogOrderStatusChange
ON Orders
AFTER UPDATE
AS
BEGIN
    IF UPDATE(OrderStatus)
    BEGIN
        DECLARE @OrderId INT;
        SELECT @OrderId = OrderId FROM inserted;
        PRINT 'Order ID: ' + CAST(@OrderId AS VARCHAR(10)) + ' status updated.';
    END;
END;