INSERT INTO Restaurant (RestaurantName, CuisineType, Address, PhoneNumber, Rating) VALUES
('Khodaldham Restaurant', 'Gujarati', 'Jasdan Road, Ahmedabad', '9876543210', 4.5),
('Spicy Tadka', 'Indian', 'CG Road, Ahmedabad', '8765432109', 4.2),
('The Italian Place', 'Italian', 'SG Highway, Ahmedabad', '7654321098', 4.8),
('Chinese Wok', 'Chinese', 'Maninagar, Ahmedabad', '6543210987', 4.0),
('South Indian Delights', 'South Indian', 'Bopal, Ahmedabad', '5432109876', 4.6),
('Punjabi Dhaba', 'Punjabi', 'Prahladnagar, Ahmedabad', '4321098765', 4.3),
('Mexican Fiesta', 'Mexican', 'Satellite, Ahmedabad', '3210987654', 4.7),
('Continental Cafe', 'Continental', 'Navrangpura, Ahmedabad', '2109876543', 4.1),
('Thai Orchid', 'Thai', 'Vastrapur, Ahmedabad', '1098765432', 4.9),
('Burger Junction', 'Fast Food', 'Thaltej, Ahmedabad', '9876501234', 3.9);


INSERT INTO Users (Username, Email, Phone, Address, Password) VALUES
('JohnDoe', 'john.doe@example.com', '9876111222', '123 Main St, Ahmedabad', 'password123'),
('JaneSmith', 'jane.smith@example.com', '8765222333', '456 Elm St, Ahmedabad', 'securepass'),
('DavidLee', 'david.lee@example.com', '7654333444', '789 Oak St, Ahmedabad', 'strongpass'),
('SarahJones', 'sarah.jones@example.com', '6543444555', '101 Pine St, Ahmedabad', 'mypassword'),
('MichaelBrown', 'michael.brown@example.com', '5432555666', '112 Maple St, Ahmedabad', 'pass1234'),
('EmilyDavis', 'emily.davis@example.com', '4321666777', '131 Cedar St, Ahmedabad', 'secure123'),
('KevinWilson', 'kevin.wilson@example.com', '3210777888', '141 Birch St, Ahmedabad', 'password456'),
('JessicaGarcia', 'jessica.garcia@example.com', '2109888999', '151 Willow St, Ahmedabad', 'pass4567'),
('BrianRodriguez', 'brian.rodriguez@example.com', '1098999000', '161 Redwood St, Ahmedabad', 'secure456'),
('AshleyMartinez', 'ashley.martinez@example.com', '9876000111', '171 Spruce St, Ahmedabad', 'pass7890');


INSERT INTO Menu (RestId, ItemName, Description, Price, Availability) VALUES
(1, 'Thali', 'Traditional Gujarati Thali', 250.00, 1),
(2, 'Butter Chicken', 'Creamy Butter Chicken', 350.00, 1),
(3, 'Margherita Pizza', 'Classic Margherita Pizza', 300.00, 1),
(4, 'Veg Manchurian', 'Veg Manchurian with Gravy', 280.00, 1),
(5, 'Masala Dosa', 'Crispy Masala Dosa', 200.00, 1),
(6, 'Chole Bhature', 'Spicy Chole with Bhature', 220.00, 1),
(7, 'Tacos', 'Spicy Mexican Tacos', 320.00, 1),
(8, 'Club Sandwich', 'Classic Club Sandwich', 260.00, 1),
(9, 'Pad Thai', 'Authentic Thai Pad Thai', 380.00, 1),
(10, 'Veg Burger', 'Veggie Burger with Fries', 180.00, 1);


INSERT INTO Orders (UserId, RestaurantId, OrderDate, TotalAmount, OrderStatus) VALUES
(1, 1, '2023-10-26 12:00:00', 250.00, 'Delivered'),
(2, 2, '2023-10-26 13:30:00', 350.00, 'Shipped'),
(3, 3, '2023-10-26 14:45:00', 300.00, 'Processing'),
(4, 4, '2023-10-26 16:00:00', 280.00, 'Delivered'),
(5, 5, '2023-10-26 17:15:00', 200.00, 'Shipped'),
(6, 6, '2023-10-26 18:30:00', 220.00, 'Processing'),
(7, 7, '2023-10-26 19:45:00', 320.00, 'Delivered'),
(8, 8, '2023-10-26 21:00:00', 260.00, 'Shipped'),
(9, 9, '2023-10-26 22:15:00', 380.00, 'Processing'),
(10, 10, '2023-10-26 23:30:00', 180.00, 'Delivered');


INSERT INTO OrderItems (OrderId, MenuId, Quantity, Price) VALUES
(1, 1, 1, 250.00),
(2, 2, 1, 350.00),
(3, 3, 1, 300.00),
(4, 4, 1, 280.00),
(5, 5, 1, 200.00),
(6, 6, 1, 220.00),
(7, 7, 1, 320.00),
(8, 8, 1, 260.00),
(9, 9, 1, 380.00),
(10, 10, 1, 180.00);

INSERT INTO DeliveryStaff (StaffName, PhoneNumber, VehicleType) VALUES
('Ramesh Kumar', '9876123456', 'Bike'),
('Suresh Patel', '8765234567', 'Scooter')


INSERT INTO DeliveryStaff (StaffName, PhoneNumber, VehicleType) VALUES
('Ramesh Kumar', '9876123456', 'Bike'),
('Suresh Patel', '8765234567', 'Scooter'),
('Anita Sharma', '7654345678', 'Bike'),
('Vijay Singh', '6543456789', 'Cycle'),
('Priya Desai', '5432567890', 'Scooter'),
('Rahul Joshi', '4321678901', 'Bike'),
('Meena Gupta', '3210789012', 'Cycle'),
('Sanjay Yadav', '2109890123', 'Scooter'),
('Kavita Mehta', '1098901234', 'Bike'),
('Deepak Rana', '9876012345', 'Cycle');


-- inner join: get restaurant names and the items ordered from them.
select r.restaurantname, m.itemname from restaurant r inner join
    menu m on r.RestaurantId = m.restid;

-- left outer join: get all users and their associated orders (if any).
select u.username,o.orderid from
    users u
left join
    orders o on u.userid = o.userid;

-- right outer join: get all orders and the users who placed them (if any).
select u.username,o.orderid
from orders o
right join
users u on o.userid = u.userid;

-- full outer join: get all users and orders, showing matches where they exist.
select u.username,
    o.orderid
from users u
full outer join
    orders o on u.userid = o.userid;

-- cross join: get all possible combinations of restaurants and users.
select
    r.restaurantname,
    u.username
from
    restaurant r
cross join
    users u;

-- example of a join of more than two tables. find all restaurants and the users who ordered from them, along with the item names.
select
    r.restaurantname,
    u.username,
    m.itemname
from restaurant r join
    orders o on r.RestaurantId = o.restaurantid
	join
    users u on o.userid = u.userid
	join
    orderitems oi on o.orderid = oi.orderid
	join
    menu m on oi.menuid = m.menuid;

---UPDATE 
update Restaurant
set rating = 4.2
where RestaurantName='Chinese Wok';

update orders 
set OrderStatus = 'Completed'
where OrderId=3

--DElete
Delete from users where Username='BrianRodriguez'

delete from orders 
where RestaurantId=10;