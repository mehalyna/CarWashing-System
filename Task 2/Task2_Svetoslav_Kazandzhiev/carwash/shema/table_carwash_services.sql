CREATE TABLE Carwash_Services (
	service_id integer NOT NULL,
	carwash_id integer NOT NULL,
	PRIMARY KEY (service_id,carwash_id),
    FOREIGN KEY (service_id) REFERENCES Services(service_id),
    FOREIGN KEY (carwash_id) REFERENCES Carwhashes(carwash_id)
);

