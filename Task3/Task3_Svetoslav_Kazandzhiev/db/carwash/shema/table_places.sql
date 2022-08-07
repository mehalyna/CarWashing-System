CREATE TABLE Places (
	place_id serial NOT NULL,
	place_name varchar(255) NOT NULL UNIQUE,
	PRIMARY KEY (place_id)

);
