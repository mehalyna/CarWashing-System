
CREATE TABLE Order_Details (
	carwash_place_id integer NOT NULL,
	service_id integer NOT NULL,
	order_id integer NOT NULL,
	price FLOAT NOT NULL,
	duration integer NOT NULL,
	start_time TIME NOT NULL,
	PRIMARY KEY (service_id,order_id),
    FOREIGN KEY (carwash_place_id) REFERENCES Carwash_Places(carwash_place_id),
    FOREIGN KEY (service_id) REFERENCES Services(service_id),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)

);
