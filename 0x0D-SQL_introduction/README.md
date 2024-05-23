# 0x0D. SQL - Introduction

![](https://upload.wikimedia.org/wikipedia/commons/8/87/Sql_data_base_with_logo.png)






# DDL AND DML(SQL Commands)

![](https://miro.medium.com/v2/resize:fit:600/0*9vY3QnX4iHr3uc3_.png)

DDL and DML are both important parts of working with databases, but they serve different purposes:

* **DDL (Data Definition Language)**:  As the name suggests, DDL is used to define and manipulate the structure of a database. This includes creating and modifying database objects like tables, views, indexes, and users.  Essentially, DDL defines the blueprint for how data will be organized within the database.

* **DML (Data Manipulation Language)**:  DML focuses on managing the data itself within the database structure created by DDL.  This includes inserting new data, updating existing data, and deleting data from the database.  DML allows you to interact with the information stored within the database.

Here's a table summarizing the key differences between DDL and DML:

| Feature                 | DDL (Data Definition Language) | DML (Data Manipulation Language) |
|--------------------------|---------------------------------|---------------------------------|
| Purpose                  | Defines database structure      | Manipulates data within structure |
| Examples of commands     | CREATE, ALTER, DROP, TRUNCATE    | INSERT, UPDATE, DELETE, SELECT  |
| Use of WHERE clause       | Not typically used              | Frequently used for filtering data |
| Impact on data            | Creates or modifies structure     | Modifies existing data           |
| Transaction permanence   | Changes are permanent            | Changes can be rolled back       |

In short, DDL creates the foundation (the database structure) and DML manages the content (the data) that resides within that foundation. They work together to effectively store and manage information in a database.
