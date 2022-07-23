CREATE TABLE IF NOT EXISTS "Carwash_Services"
(
    service_id integer,
    carwash_id integer,
    PRIMARY KEY (service_id, carwash_id),
    CONSTRAINT service_id FOREIGN KEY (service_id)
        REFERENCES public."Services" (service_id),
    CONSTRAINT carwash_id FOREIGN KEY (carwash_id)
        REFERENCES public."Carwashes" (carwash_id)
);
