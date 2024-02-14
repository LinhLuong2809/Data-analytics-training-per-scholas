# Combonent 1: Creating indexes for Query Performance
-- index for customers table on last_name
create index idx_last_name on customers(last_name);

-- index for customers table on registration_date
create index idx_registration_date on customers(registration_date);

-- index for orders table on order date
create index idx_order_date on orders(order_date);

-- index for products table on category
create index idx_category on products(category);

# Combonent 2: Database Constraints
-- implement primary key constraints for all provided tables.
Alter Table customers
Add Primary Key(customer_id);

Alter Table orderdetails
Add Primary Key(order_detail_id);

Alter Table orders
Add Primary Key(order_id);

Alter Table products
Add Primary Key(product_id);

-- Set up foreign key constraints between Orders and Customers
Alter table orders
Add constraint orders_customers_fk
foreign key (customer_id)
references Customers(customer_id);

-- Set up foreign key constraints between OrderDetails, Orders, and Products.
Alter table orderdetails
Add constraint orderdetails_orders_fk foreign key (order_id) references orders(order_id),
Add constraint orderdetails_products_fk foreign key (product_id) references products(product_id);

-- Add a check constraint on Products.price to ensure it is greater than zero.
Alter table products
add constraint check_price Check (price > 0);

#3 Component 3: Database Triggers
-- Create a trigger on OrderDetails that updates total_amount in Orders whenever a new order detail is added or an existing one is updated.
DELIMITER //
-- create trigger after insert value to orderdetails table
Create Trigger update_total_amount_after_insert 
After Insert on orderdetails
for each row
-- trigger statement where it automatically update total_amount value in table orders whenever a new value is inserted into orderdetails table
Begin
	update orders -- start update order table
    Set total_amount = ( select coalesce((quantity*unit_price), 0) from orderdetails where order_id = new.order_id) -- this line of code update total_amount when we insert new value for orderdetails table and return 0 if value is null by calling coalesce() build in function
    where order_id = new.order_id; -- condition to update the order table where the new order_id is inserted. 
end ;
//

-- create trigger after update value to orderdetails table
-- this trigger work the same as the above trigger, the only difference is this trigger call after update values in orderdetails table 
Create Trigger update_total_amount_after_update
After update on orderdetails -- this line of code is the only different that check for after update on orderdetails to trigger. the rest of the code is similar when insert value
for each row
Begin
	update orders
    Set total_amount = ( select coalesce((quantity*unit_price), 0) from orderdetails where order_id = new.order_id)
    where order_id = new.order_id;
end ;
//
DELIMITER ;

-- Create a trigger on Customers that logs changes to address in a new table AddressChangeLog.
-- first we need to create a new table AddressChangeLog with value as log_id, customer_id, old address and new address changed with foreign key reference to the customers table
create table AddressChangeLog (
	log_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    old_address_street VARCHAR(255),
    old_address_city VARCHAR(255),
    old_address_state VARCHAR(255),
    old_address_postal_code VARCHAR(20),
    new_address_street VARCHAR(255),
    new_address_city VARCHAR(255),
    new_address_state VARCHAR(255),
    new_address_postal_code VARCHAR(20),
    foreign key (customer_id) references customers(customer_id)
);

-- create trigger on customer table for address change
DELIMITER //
create trigger address_change_trigger
after update on customers
for each row
-- statement to update addresschangelog with all possible cases when you update any new address as city, state, street, postal code it will insert the log to addresschangelog old address and new address.
begin
	If old.address_street <> new.address_street and old.address_city <> new.address_city and old.address_state <> new.address_state and old.address_postal_code <> new.address_postal_code  then
		insert into AddressChangeLog (customer_id,old_address_street,old_address_city,old_address_state,old_address_postal_code,new_address_street,new_address_city,new_address_state,new_address_postal_code)
        values (old.customer_id, old.address_street, old.address_city, old.address_state,old.address_postal_code, new.address_street, new.address_city, new.address_state,new.address_postal_code);
        
	elseIf old.address_street <> new.address_street and old.address_city <> new.address_city and old.address_state <> new.address_state then
		insert into AddressChangeLog (customer_id,old_address_street,old_address_city,old_address_state,old_address_postal_code,new_address_street,new_address_city,new_address_state,new_address_postal_code)
        values (old.customer_id, old.address_street, old.address_city, old.address_state,old.address_postal_code, new.address_street, new.address_city, new.address_state,old.address_postal_code);
	
    elseIf old.address_street <> new.address_street and old.address_city <> new.address_city and old.address_postal_code <> new.address_postal_code then
		insert into AddressChangeLog (customer_id,old_address_street,old_address_city,old_address_state,old_address_postal_code,new_address_street,new_address_city,new_address_state,new_address_postal_code)
        values (old.customer_id, old.address_street, old.address_city, old.address_state,old.address_postal_code, new.address_street, new.address_city, old.address_state,new.address_postal_code);

	elseIf old.address_street <> new.address_street and old.address_state <> new.address_state and old.address_postal_code <> new.address_postal_code then
		insert into AddressChangeLog (customer_id,old_address_street,old_address_city,old_address_state,old_address_postal_code,new_address_street,new_address_city,new_address_state,new_address_postal_code)
        values (old.customer_id, old.address_street, old.address_city, old.address_state,old.address_postal_code, new.address_street, old.address_city, new.address_state,new.address_postal_code);
	
    elseIf old.address_city <> new.address_city and old.address_state <> new.address_state and old.address_postal_code <> new.address_postal_code then
		insert into AddressChangeLog (customer_id,old_address_street,old_address_city,old_address_state,old_address_postal_code,new_address_street,new_address_city,new_address_state,new_address_postal_code)
        values (old.customer_id, old.address_street, old.address_city, old.address_state,old.address_postal_code, old.address_street, new.address_city, new.address_state,new.address_postal_code);
        
	elseIf old.address_state <> new.address_state and old.address_postal_code <> new.address_postal_code then
		insert into AddressChangeLog (customer_id,old_address_street,old_address_city,old_address_state,old_address_postal_code,new_address_street,new_address_city,new_address_state,new_address_postal_code)
        values (old.customer_id, old.address_street, old.address_city, old.address_state,old.address_postal_code, old.address_street, old.address_city, new.address_state,new.address_postal_code);

	elseIf old.address_city <> new.address_city and old.address_postal_code <> new.address_postal_code then
		insert into AddressChangeLog (customer_id,old_address_street,old_address_city,old_address_state,old_address_postal_code,new_address_street,new_address_city,new_address_state,new_address_postal_code)
        values (old.customer_id, old.address_street, old.address_city, old.address_state,old.address_postal_code, old.address_street, new.address_city, old.address_state,new.address_postal_code);
        
	elseIf old.address_street <> new.address_street and old.address_postal_code <> new.address_postal_code then
		insert into AddressChangeLog (customer_id,old_address_street,old_address_city,old_address_state,old_address_postal_code,new_address_street,new_address_city,new_address_state,new_address_postal_code)
        values (old.customer_id, old.address_street, old.address_city, old.address_state,old.address_postal_code, new.address_street, old.address_city, old.address_state,new.address_postal_code);
        
	elseIf old.address_state <> new.address_state and old.address_city <> new.address_city then
		insert into AddressChangeLog (customer_id,old_address_street,old_address_city,old_address_state,old_address_postal_code,new_address_street,new_address_city,new_address_state,new_address_postal_code)
        values (old.customer_id, old.address_street, old.address_city, old.address_state,old.address_postal_code, old.address_street, new.address_city, new.address_state,old.address_postal_code);
        
	elseIf old.address_state <> new.address_state and old.address_street <> new.address_street then
		insert into AddressChangeLog (customer_id,old_address_street,old_address_city,old_address_state,old_address_postal_code,new_address_street,new_address_city,new_address_state,new_address_postal_code)
        values (old.customer_id, old.address_street, old.address_city, old.address_state,old.address_postal_code, new.address_street, old.address_city, new.address_state, old.address_postal_code);
	
    elseIf old.address_street <> new.address_street and old.address_city <> new.address_city then
		insert into AddressChangeLog (customer_id,old_address_street,old_address_city,old_address_state,old_address_postal_code,new_address_street,new_address_city,new_address_state,new_address_postal_code)
        values (old.customer_id, old.address_street, old.address_city, old.address_state,old.address_postal_code, new.address_street, new.address_city, old.address_state,old.address_postal_code);
	
    elseIf old.address_street <> new.address_street then
		insert into AddressChangeLog (customer_id,old_address_street,old_address_city,old_address_state,old_address_postal_code,new_address_street,new_address_city,new_address_state,new_address_postal_code)
        values (old.customer_id, old.address_street, old.address_city, old.address_state,old.address_postal_code, new.address_street, old.address_city, old.address_state,old.address_postal_code);
	
    elseIf old.address_city <> new.address_city then
		insert into AddressChangeLog (customer_id,old_address_street,old_address_city,old_address_state,old_address_postal_code,new_address_street,new_address_city,new_address_state,new_address_postal_code)
        values (old.customer_id, old.address_street, old.address_city, old.address_state,old.address_postal_code, old.address_street, new.address_city, old.address_state,old.address_postal_code);
        
	elseIf old.address_state <> new.address_state then
		insert into AddressChangeLog (customer_id,old_address_street,old_address_city,old_address_state,old_address_postal_code,new_address_street,new_address_city,new_address_state,new_address_postal_code)
        values (old.customer_id, old.address_street, old.address_city, old.address_state,old.address_postal_code, old.address_street, old.address_city, new.address_state, old.address_postal_code);
	
    else
		insert into AddressChangeLog (customer_id,old_address_street,old_address_city,old_address_state,old_address_postal_code,new_address_street,new_address_city,new_address_state,new_address_postal_code)
        values (old.customer_id, old.address_street, old.address_city, old.address_state,old.address_postal_code, old.address_street, old.address_city, old.address_state, new.address_postal_code);
    end if;
end;
//
DELIMITER ;

update customers set address_street = '102 gold medal dr', address_city = 'Baton Rouge' where customer_id = 1;

# Combonent 4: Database Views
-- Create a view named CustomerOrderDetailView that joins Customers, Orders, and OrderDetails.
create view CustomerOrderDetailView As
select customer_id, first_name, last_name, order_id, product_id, quantity, unit_price from customers
join orders using(customer_id)
join orderdetails using(order_id);

-- sample query
select * from customerorderdetailview;

# Component 5: Advanced SQL Queries
-- Write a query to find the top 3 customers with the highest total spending.
-- I select total_amount from orders table and join with customers table then sort the total amount spending in descending order and limit with only 3 results to find the top 3 customers with highest total spending. 
select concat(first_name, ' ', last_name) as customers_name, total_amount
from customers
join orders using(customer_id)
order by total_amount desc
limit 3;

-- Write a query to find the most popular product category.
-- I sum all the quantity from orderdetails table join products table to find the total items that sold and group by category. 
-- Items that were orderd with the highest number would be the popular product category.
select category, sum(quantity) as total_items_ordered
from products 
join orderdetails using(product_id)
group by category
order by total_items_ordered desc
limit 1;

# Component 6: Trigger Management
-- Create a trigger on Products that updates a ProductAudit table whenever a product's price is changed.
-- first we create ProductAudit table
create table ProductAudit(
	log_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    old_price DECIMAL (10,2),
    new_price DECIMAL (10,2),
    foreign key (product_id) references products(product_id)
);

-- create trigger on products
Delimiter //
create trigger update_productAudit_trigger
after update on products
for each row
begin
	if old.price <> new.price then -- conditions to check if the updated price is different from the old price to trigger
		insert into ProductAudit(product_id, old_price, new_price) -- insert values to productAudit with the change relate to the products
        values (old.product_id, old.price, new.price);
	end if;
end;
// 
Delimiter ;
-- Modify this trigger to also log changes in the product's category.
-- first we need to update our productAudittable to have column for old category and new update category
Alter Table ProductAudit
Add column old_category VARCHAR(255), Add column new_category VARCHAR(255);

-- modify the trigger to also log changes in the product's category
-- because mySQL doesn't have statement to update an existing trigger in the query, we can edit by right click on table name and chose alter table oftion to pick trigger option 
-- and alter it. Otherwise, we have to drop it and create a new one
Delimiter //
drop trigger if exists update_productAudit_trigger; -- drop exists trigger
create trigger update_productAudit_trigger -- create trigger to modify
after update on products
for each row
begin
	if old.price <> new.price or old.category <> new.category then -- conditions to check if the updated price is different from the old price or the new category differ from old category to trigger
		insert into ProductAudit(product_id, old_price, new_price, old_category, new_category) -- insert values to productAudit with the change relate to the products
        values (old.product_id, old.price, new.price, old.category, new.category);
	end if;
end;
// 
Delimiter ;

-- Write an SQL statement to delete this trigger.
drop trigger if exists update_productAudit_trigger;

# Component 7: Database Views Management
-- Create a view BusinessScenarioView combining Customers, Orders, and Products.
-- since customer and order doesn't have any foreign key to combine with products table, we have to combinne with orderdetails table to combine with products table
create view BusinessScenarioView as
select * from customers
join orders using(customer_id)
join orderdetails using(order_id)
join products using(product_id);

-- sample query
select * from BusinessScenarioView;

-- modify views to only include order_date and email
alter view BusinessScenarioView as
select order_date, email
from customers
join orders using(customer_id)
join orderdetails using(order_id)
join products using(product_id);

-- sample query
select * from BusinessScenarioView;

-- Write an SQL statement to delete BusinessScenarioView.
drop view if exists BusinessScenarioView;
-- the reason why we delete a view is when it's no longer useful or when we need to make a change so we drop the view and create a new one. 
-- an alternative way to delete a view is using mysql workbench, right click on the view you want to delete in the schemas and select the option drop view...
