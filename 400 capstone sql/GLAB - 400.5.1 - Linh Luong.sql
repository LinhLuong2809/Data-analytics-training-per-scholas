# To do 1
-- create user data_analyst
create user 'data_analyst'@'localhost' identified by 'dataanalyst';
-- grant select on customer table
Grant select on data_sentry.customers to 'data_analyst'@'localhost';

-- revoke select privilage
revoke select on data_sentry.customers from 'data_analyst'@'localhost';

# To do 2

-- create role manager
create role 'manager';

-- grant privileges
grant select, insert, update on data_sentry.employees to 'manager';

-- create user account team lead
create user 'team_lead' identified by 'teamlead';
SET PERSIST mandatory_roles = 'manager';

-- grant role to team lead user
grant 'manager' to 'team_lead';

show grants for 'team_lead';

# To do 3
-- create user account data_entry with password "data123"
create user 'data_entry' identified by 'data123';

-- grant insert privilege
grant insert on data_sentry.orders to 'data_entry';