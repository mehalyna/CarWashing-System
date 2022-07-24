CREATE TABLE Carwash_Places (
	carwash_place_id serial NOT NULL,
	place_id integer NOT NULL,
	car_wash_id integer NOT NULL,
	is_free BOOLEAN NOT NULL,
	PRIMARY KEY (carwash_place_id),
    FOREIGN KEY (place_id) REFERENCES Places(place_id),
    FOREIGN KEY (car_wash_id) REFERENCES car_washes(car_wash_id)

);
