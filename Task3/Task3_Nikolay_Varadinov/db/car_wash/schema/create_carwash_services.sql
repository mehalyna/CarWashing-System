CREATE TABLE carwash_services (
    service_id integer,
    carwash_id integer,
    CONSTRAINT carwash_services_pk PRIMARY KEY (service_id, carwash_id),
    CONSTRAINT services_fk0 FOREIGN KEY (service_id) REFERENCES services(service_id),
    CONSTRAINT carwashes_fk1 FOREIGN KEY (carwash_id) REFERENCES carwashes(carwash_id),
);
