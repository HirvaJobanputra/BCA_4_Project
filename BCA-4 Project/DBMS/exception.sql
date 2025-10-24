-- example 1: handling duplicate restaurant name
begin try
    insert into restaurant (restaurantname, cuisinetype, address, phonenumber, rating)
    values ('khodaldham restaurant', 'another cuisine', 'new address', '1112223333', 4.0); -- duplicate restaurantname
end try
begin catch
    select error_message() as errormessage, error_severity() as errorseverity, error_state() as errorstate;
end catch;

-- example 2: handling invalid user id in orders 



begin try
    insert into orders (userid, restaurantid, totalamount)
    values (99999, 1, 150.00); -- invalid userid
end try
begin catch
    select error_message() as errormessage, error_severity() as errorseverity, error_state() as errorstate;
end catch;

-- example 3: handling invalid restaurant id in menu -------
begin try
    insert into menu (restid, itemname, price)
    values (99999, 'invalid item', 10.00); -- invalid restid
end try
begin catch
    select error_message() as errormessage, error_severity() as errorseverity, error_state() as errorstate;
end catch;

-- example 4: handling invalid order id in orderitems-------
begin try
    insert into orderitems (orderid, menuid, quantity, price)
    values (99999, 1, 1, 10.00); -- invalid orderid
end try
begin catch
    select error_message() as errormessage, error_severity() as errorseverity, error_state() as errorstate;
end catch;



--- example 5: handling invalid menu id in orderitems (foreign key violation)---------
begin try
    insert into orderitems (orderid, menuid, quantity, price)
    values (1, 99999, 1, 10.00); -- invalid menuid
end try
begin catch
    select error_message() as errormessage, error_severity() as errorseverity, error_state() as errorstate;
end catch;