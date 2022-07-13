CREATE TABLE Orders (
	order_id serial NOT NULL,
	carwash_id integer NOT NULL,
	user_id integer NOT NULL,
	order_current_status varchar(20) NOT NULL,
	order_date_time TIMESTAMP NOT NULL,
	execution TIMESTAMP NOT NULL,
	PRIMARY KEY (order_id),
    FOREIGN KEY (carwash_id) REFERENCES Carwhashes(carwash_id),
    FOREIGN KEY (user_id) REFERENCES "Users"(user_id)
);
