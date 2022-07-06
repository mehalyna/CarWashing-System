
#Start creating DB model

CREATE TABLE Users (
	"user_id" serial NOT NULL,
	"phone_number" varchar(15) NOT NULL UNIQUE,
	"full_name" varchar(255) NOT NULL,
	"user_location" varchar(255) NOT NULL,
	PRIMARY KEY ("user_id")

);

CREATE TABLE Places (
	"place_id" serial NOT NULL,
	"place_name" varchar(255) NOT NULL UNIQUE,
	PRIMARY KEY ("place_id")

);

CREATE TABLE Services (
	"service_id" serial NOT NULL,
	"service_name" varchar(255) NOT NULL UNIQUE,
	PRIMARY KEY ("service_id")

);

#AND SO ON until we create the DB model

#Insert some data 

INSERT INTO users (
    user_id
    , phone_number
    , full_name
    , user_location
    ) 
    VALUES (
        2
        , '0900290099'
        , 'Ivan Ivanov'
        , 'Plovdiv'
    );
    
INSERT INTO users (
    user_id
    , phone_number
    , full_name
    , user_location
    ) 
    VALUES (
        3
        , '0870933299'
        , 'Gosho Toshev'
        , 'Bourgas'
    );
    
insert into accounts (
    account_id
    ,user_id
    ,email
    ,password
)
VALUES (
    1
    ,1
    ,'pesho@abv.bg'
    ,'qwerty'
);   
 
    
 #Schema is ready
 
 dev=# \dt
             List of relations
 Schema |       Name       | Type  | Owner 
--------+------------------+-------+-------
 public | accounts         | table | dev
 public | carwash_places   | table | dev
 public | carwash_services | table | dev
 public | carwhashes       | table | dev
 public | order_details    | table | dev
 public | orders           | table | dev
 public | places           | table | dev
 public | services         | table | dev
 public | users            | table | dev
(9 rows)


#Playing with data

dev=# 	SELECT *
	FROM Users
	INNER JOIN Accounts  ON true;
	
 user_id | phone_number |  full_name   | user_location | account_id | user_id |    email     | password 
---------+--------------+--------------+---------------+------------+---------+--------------+----------
       2 | 0900290099   | Ivan Ivanov  | Plovdiv       |          1 |       1 | pesho@abv.bg | qwerty
       3 | 0870933299   | Gosho Toshev | Bourgas       |          1 |       1 | pesho@abv.bg | qwerty
       1 | 0870990099   | Pesho Petkoc | Sofia         |          1 |       1 | pesho@abv.bg | qwerty
(3 rows)


dev=# SELECT
        Users.user_id,
    	phone_number,
        account_id
      FROM
        Users
      LEFT JOIN Accounts
    ON Accounts.account_id = Users.user_id
WHERE Accounts.account_id IS NULL;

 user_id | phone_number | account_id 
---------+--------------+------------
       2 | 0900290099   |           
       3 | 0870933299   |           
(2 rows)

