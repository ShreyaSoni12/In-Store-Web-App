CREATE DATABASE DEMO;
USE DEMO;
CREATE TABLE loan (loan_id int AUTO_INCREMENT, 
                   name varchar(100),
                   address varchar(100),
                   amount int,
                   item_type varchar(20),
                   description varchar(200),
                   loan_date DATETIME NOT NULL DEFAULT NOW(),
                   settle_loan varchar(10) DEFAULT 'NO',
                   PRIMARY KEY (loan_id));