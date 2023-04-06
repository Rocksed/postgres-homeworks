-- SQL-команды для создания таблиц
CREATE TABLE employees
(
    first_name varchar(100),
    last_name varchar(100),
    title varchar(100),
    birth_date char(100),
    notes text
);

CREATE TABLE customers
(
    customer_id varchar(100),
    company_name varchar(100),
    contact_name varchar(100)
);

CREATE TABLE orders
(
    order_id int PRIMARY KEY,
    customer_id varchar(100),
    employee_id int,
    order_date varchar(100),
    ship_city  varchar(100)
);