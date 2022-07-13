CREATE TABLE Carwash_Places (
	carwash_place_id serial NOT NULL,
	place_id integer NOT NULL,
	carwash_id integer NOT NULL,
	is_free BOOLEAN NOT NULL,
	PRIMARY KEY (carwash_place_id),
    FOREIGN KEY (place_id) REFERENCES Places(place_id),
    FOREIGN KEY (carwash_id) REFERENCES Carwhashes(carwash_id)

);
