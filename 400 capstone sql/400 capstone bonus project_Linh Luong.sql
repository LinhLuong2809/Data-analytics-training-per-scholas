# Database Compromise Investigation (400)
# Objective: Identify unauthorized changes in the database.

-- tasks:
-- Analyze Logs: Examine db_logs_df for suspicious activities, focusing on unusual patterns in operations (like unexpected DELETE operations).
select * from db_logs
where operation like 'DELETE'
order by timestamp;

-- Identify Anomalies: Look for anomalies in timestamps, such as activities occurring at odd hours.
select * from event_data 
where hour(timestamp) > 0 and hour(timestamp) < 6
order by timestamp;

-- Trace Changes: Correlate suspicious activities with changes in other datasets (like sudden changes in people_df or transaction_df).
-- create trigger to trace changes in people_data 
-- trigger to update db_logs after insert, update, delete name in people_data.

-- insert trigger
create trigger insert_people_trigger
after insert on people_data
for each row 
	insert db_logs values(current_timestamp, 'INSERT', new.name);

-- update trigger
create trigger update_people_trigger
after update on people_data
for each row 
	insert db_logs values(current_timestamp, 'UPDATE', new.name);

-- delete trigger
create trigger after_delete_people_data
after delete on people_data
for each row 
	insert into db_logs values(current_timestamp, 'DELETE', old.name);

-- trigger to update db_logs after insert, update, delete user id in transaction_data.
-- insert trigger 
create trigger insert_transaction_trigger
after insert on transaction_data
for each row 
	insert db_logs values(current_timestamp, 'INSERT', new.user_id);

-- update trigger
create trigger update_transaction_trigger
after update on transaction_data
for each row 
	insert db_logs values(current_timestamp, 'UPDATE', new.user_id);
    
-- delete trigger
create trigger after_delete_transaction_data
after delete on transaction_data
for each row 
	insert into db_logs values(current_timestamp, 'DELETE', old.user_id);
    
-- testing trigger on people data table
insert people_data values('Linh Luong', '234 lafatea dreerd dr', 'linhldafg@gmail.com');
update people_data set name = 'Sam Sung' where name like 'Linh Luong';
delete from people_data where name like 'Sam Sung';
select * from db_logs order by timestamp desc;

-- testing trigger on transaction data table
insert transaction_data values ('@1241243dfaskafak324112l', 'Linh Luong', 23190.35, curdate(), 'Toyota');
select * from db_logs order by timestamp desc;
