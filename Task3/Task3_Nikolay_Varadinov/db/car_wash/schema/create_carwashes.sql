CREATE TABLE carwashes (
    carwash_id integer,
    carwash_name character varying (15),
    _address character varying,
    quantity_of_places smallint,
    CONSTRAINT carwashes_pk PRIMARY KEY (carwash_id),
);
