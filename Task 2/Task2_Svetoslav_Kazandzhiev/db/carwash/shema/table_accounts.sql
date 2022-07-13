CREATE TABLE Accounts (
	account_id serial NOT NULL,
	user_id serial NOT NULL,
	email varchar(50) NOT NULL,
	password varchar(50) NOT NULL,
	PRIMARY KEY ("account_id"),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
