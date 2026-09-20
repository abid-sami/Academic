create database myDB;

use myDB;

create table stu(
    id INT,
    name varchar(20),
    dept varchar(5),
    cgpa Decimal(3,2)
);

insert into stu values(101,'Sami', 'CSE', 3.50); 
insert into stu values(102,'Karim', 'BBA', 3.80); 
insert into stu values(103,'Sumi', 'EEE', 3.20); 

insert into stu (id, name, dept, cgpa) 
values(104,'Rafi', 'CSE', 3.80); 

truncate table stu;

select * from stu;

drop table stu;