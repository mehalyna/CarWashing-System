CREATE TABLE "Carwashes"
(
    carwash_id integer,
    carwash_name character varying(50) NOT NULL,
    address character varying(50) NOT NULL,
    quantity_of_places integer NOT NULL,
    PRIMARY KEY (carwash_id)
);
