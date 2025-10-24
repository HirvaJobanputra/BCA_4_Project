--1 get order details
create procedure getorderdetails
    @orderid int
as
begin
    select m.itemname, oi.quantity, oi.price
    from orderitems oi
    join menu m on oi.menuid = m.menuid
    where oi.orderid = @orderid;
end;

exec getorderdetails 1
--2 update orders
create procedure updateorderstatus
    @orderid int,
    @orderstatus varchar(50)
as
begin
    update orders
    set orderstatus = @orderstatus
    where orderid = @orderid;
end;

exec updateorderstatus 1, Delivered

--3 add/update menu item
create procedure addupdatemenuitem
    @menuid int = null,
    @restaurantid int,
    @itemname varchar(255),
    @description text,
    @price decimal(5, 2),
    @availability bit
as
begin
    if @menuid is null
    begin
        -- insert new item
        insert into menu (restid, itemname, description, price, availability)
        values (@restaurantid, @itemname, @description, @price, @availability);
    end
    else
    begin
        -- update existing item
        update menu
        set restid = @restaurantid,
            itemname = @itemname,
            description = @description,
            price = @price,
            availability = @availability
        where menuid = @menuid;
    end;
end;
exec addupdatemenuitem 101

--4 assign delivery item
create procedure assigndeliverystaff
    @orderid int,
    @deliverystaffid int
as
begin
    update orders
    set deliverystaffid = @deliverystaffid,
        orderstatus = 'out for delivery' 
    where orderid = @orderid;
end;

--5. place an order
create procedure getuserfullname
    @userid int
as
begin
    select username as fullname
    from users
    where userid = @userid;
end;

exec getuserfullname 1

-- 6. DELETE AN ORDER
CREATE PROCEDURE DELETE_USERNAME