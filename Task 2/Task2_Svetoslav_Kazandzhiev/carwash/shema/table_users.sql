CREATE TABLE Users (
	user_id serial NOT NULL,
	phone_number varchar(15) NOT NULL UNIQUE,
	full_name varchar(255) NOT NULL,
	user_location varchar(255) NOT NULL,
	PRIMARY KEY (user_id)

);

