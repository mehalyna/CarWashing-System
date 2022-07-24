CREATE TABLE Carwash_Services (
	service_id integer NOT NULL,
	car_wash_id integer NOT NULL,
	PRIMARY KEY (service_id,car_wash_id),
    FOREIGN KEY (service_id) REFERENCES Services(service_id),
    FOREIGN KEY (car_wash_id) REFERENCES car_washes(car_wash_id)
);

