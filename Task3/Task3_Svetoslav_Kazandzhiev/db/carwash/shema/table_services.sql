CREATE TABLE Services (
	service_id serial NOT NULL,
	service_name varchar(255) NOT NULL UNIQUE,
	PRIMARY KEY (service_id)

);
