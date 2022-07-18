CREATE TABLE IF NOT EXISTS "Carwash_Places"
(
    carwash_place_id integer,
    place_id integer,
    carwash_id integer,
    is_free boolean,
    PRIMARY KEY (carwash_place_id),
    CONSTRAINT place_id FOREIGN KEY (place_id)
        REFERENCES public."Places" (place_id) MATCH SIMPLE,
    CONSTRAINT carwash_id FOREIGN KEY (carwash_id)
        REFERENCES public."Carwashes" (carwash_id) MATCH SIMPLE
);
