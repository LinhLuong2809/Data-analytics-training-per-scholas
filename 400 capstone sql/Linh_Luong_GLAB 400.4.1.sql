# To do 1
-- 1 create trigger update stock
DELIMITER //
create trigger update_stock
before update on products
for each row

-- 2 implement trigger statement to verify quantityinstock >= 0
begin
	If NEW.quantityInStock < 0 THEN
    SIGNAL SQLSTATE '45000'
	SET MESSAGE_TEXT = 'quantity cannot be less than 0 please update with positive value';
    end IF;
end;
DELIMITER ;

-- 3 test the trigger
update products set quantityInStock = 7933 Where productCode = 'S10_1678';

# To do 2
DELIMITER //
Drop trigger if exists update_stock;

create trigger update_stock 
before update on products
for each row

begin
	If NEW.quantityInStock < 0 OR NEW.quantityInStock > 100 THEN
    SIGNAL SQLSTATE '45000'
	SET MESSAGE_TEXT = 'quantity cannot be less than 0 or exceed 100';
    end IF;
end;
DELIMITER ;
update products set quantityInStock = 200 Where productCode = 'S10_1678';

# todo 3
drop table if exists logUpdate;
create table `logUpdate` (
    `log_id` INT AUTO_INCREMENT PRIMARY KEY,
	`orderNumber` int,
	`orderDate` date,
	`requiredDate` date,
	`shippedDate` date DEFAULT NULL,
	`status` varchar(15),
	`comments` text,
	`customerNumber` int,
	`operation_type` VARCHAR(10)
    );
    
DELIMITER //
create trigger log_changes
after update on orders
for each row

begin

    Insert into logUpdate (orderNumber, orderDate, requiredDate, shippedDate, status , comments, customerNumber, operation_type)
    values (New.orderNumber, NEw.orderDate, NEw.requiredDate, NEw.shippedDate, New.status, new.comments, new.customerNumber,'UPDATE');

end;

DELIMITER ;

update orders set comments = 'good' Where orderNumber = '10100';

Select * from logUpdate;

-- 2 delete log changes
drop trigger log_changes;


