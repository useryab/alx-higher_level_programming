# 1. 0x0D. SQL - Introduction

![](https://upload.wikimedia.org/wikipedia/commons/8/87/Sql_data_base_with_logo.png)

## 1.1. Resources

*
*
*
*
*

## 1.2. Databases

### 1.2.1. Relational databases (RDB)

#### 1.2.1.1. Relational Database Management Systems(RDBMS)

Help users create and maintain a relational database

* mySQL
* Oracle
* PostgreSQL
* MariaDB

| Student Id | Name   | major     |
| ---------- | ------ | --------- |
| 1          | Jack   | Biology   |
| 2          | Kate   | Sociology |
| 3          | Claire | English   |
| 4          | Jack   | Biology   |
| 5          | Mike   | Comp.sci  |

* primary Key: Uniquely identify specific row(Student Id)

| email                  | password  | date_created | Type    |
| ---------------------- | --------- | ------------ | ------- |
| <fakeemail@fake.co>    | shivers1  | 1999-05-11   | Admin   |
| <fakeemail112@fake.co> | wordpass  | 2001-03-15   | Free    |
| <fake@fake.co>         | redRoad23 | 2010-09-05   | Free    |
| <j.doe@fake.co>        | passw0rd  | 2008-06-25   | Premium |
| <fakeemail01@fake.co>  | 557df32d  | 2003-07-22   | Free    |

* Primary Key: email
* Surrogate key(type of primary key): a key that has no mapping int the real world(Employee Id)
* Natural Key: has a purpose or mapping in the real world(Social Security Numbers)
* Foreign Key: Link to another table (DB) defines relationships
* Composite Key: key that needs two attributes

### 1.2.2. Non Relational Database (NRDB)

#### 1.2.2.1. Document

* JSON
* BLOB
* XML

#### 1.2.2.2. Graph

* Relational Nodes

#### 1.2.2.3. Key-Value Hash

keys are mapped to values(string, JSON, BLOB)

#### 1.2.2.4. Non Relational Gatabases

nonrelational database management systems

* help users create and maintain a non relational database
* ** mongoDB
* ** dynamoDB
* ** apache cassandra
* ** firebase

* Are implementation specific
* ** any non relational datbse falls under this category there are no set language standard
* ** most NRDBMS will implement their own language for performing C.R.U.D and administrative operations on the database

### 1.2.3. Database Queries

Queries are requests made to the database management system for specific information

as the databases structure become more complex  it becomes more difficult to get the specific pieces of information we  want

## 1.3. What is SQL(Structured Query Language)

is a standardized language for interacting with RDBMS

used to perform C.R.U.D operations as well as other administrative tasks(user management, security,backup, etc)

used to define tables and structures

SQL code is not always Portable to other RDBMS without modification

* Create, Retrieve, Update & Delete data
* Create & manage databases
* Design & Create database tables
* perform administration tasks(Security, user management, import/export, etc)

SQL is 4 Types of languages in one

![](https://miro.medium.com/v2/resize:fit:600/0*9vY3QnX4iHr3uc3_.png)

### 2. DDL, DML, DQL & DCL(SQL Commands)

![](https://media.geeksforgeeks.org/wp-content/uploads/20210920153429/new.png)

are all important parts of working with databases, but they serve different purposes:

* **DDL (Data Definition Language)**:  As the name suggests, DDL is used to define and manipulate the structure of a database. This includes creating and modifying database objects like tables, views, indexes, and users.  Essentially, DDL defines the blueprint for how data will be organized within the database.

* **DML (Data Manipulation Language)**:  DML focuses on managing the data itself within the database structure created by DDL.  This includes inserting new data, updating existing data, and deleting data from the database.  DML allows you to interact with the information stored within the database.

* **DCL (Data Control Language)**: DCL includes commands such as GRANT and REVOKE which mainly deal with the rights, permissions, and other controls of the database system.

* **DQL (Data Query Language)**: it is a component of SQL statement that allows getting data from the database and imposing order upon it. It includes the SELECT statement.
This command allows getting the data out of the database to perform operations with it. When a SELECT is fired against a table or tables the result is compiled into a further temporary table, which is displayed or perhaps received by the program

here's a table summarizing the key differences between DDL, DML, DQL, and DCL:

| Feature                              | Description                                                                                                                                             | Example                                                                                                                  |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **DDL (Data Definition Language)**   | Used to define and manage the structure of a database. This includes creating tables, views, indexes, and constraints.                                  | *`CREATE TABLE` to create a new table* `ALTER TABLE` to modify an existing table  * `DROP TABLE` to delete a table       |
| **DML (Data Manipulation Language)** | Used to modify existing data within a database. This includes inserting new data, updating existing data, and deleting data.                            | *`INSERT` to add new rows to a table* `UPDATE` to modify existing data in a table * `DELETE` to remove rows from a table |
| **DQL (Data Query Language)**        | Used to retrieve data from a database.  DQL statements do not modify the data itself.                                                                   | * `SELECT` to retrieve data from one or more tables                                                                      |
| **DCL (Data Control Language)**      | Used to manage access control to the database. This includes granting and revoking permissions for users to perform various operations on the database. | *`GRANT` to give a user permission to perform an action* `REVOKE` to take away a user's permission to perform an action  |
