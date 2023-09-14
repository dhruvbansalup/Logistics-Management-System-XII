-- Creating Main Database LMS
create database if not exists LMS;

-- Using Database LMS
use LMS;

-- Creating Tables

create table if not exists Consigners
(ConsignerId bigint not null auto_increment,
ConsignerName varchar(50),
ConsignerMob bigint(10),
ConsignerAddress varchar(250),
ConsignerPinCode bigint(6),

primary key(ConsignerId));

create table if not exists Consignees
(ConsigneeId bigint not null auto_increment,
ConsigneeName varchar(50),
ConsigneeMob bigint(10),
ConsigneeAddress varchar(250),
ConsigneePinCode bigint(6),

primary key(ConsigneeId));

create table if not exists Orders
(OrderDate date not null default (current_date()),
OrderId bigint not null auto_increment,
ConsignerId bigint not null,
ConsigneeId bigint not null,
ItemName varchar(250),
qty varchar(50),
DistanceKM bigint not null,

Primary key(OrderId),
Foreign key (ConsignerId) references Consigners(ConsignerId),
foreign key (ConsigneeId) references Consignees(ConsigneeID));

create table if not exists Invoices
(InvoiceDate Date not null default (current_date()),
InvoiceNo bigint not null auto_increment,
OrderId bigint not null,
RatePerKM bigint not null,

Primary Key (invoiceNo),
foreign key (OrderId) references Orders(OrderId));

create table if not exists Employees(
EmployeeID bigint(3) not null auto_increment,
Name varchar(50) not null,
Mob bigint(10),
Address varchar(250),
Date_of_Joining date default (current_date()),
primary key (EmployeeID));

