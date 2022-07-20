CREATE TABLE carwash_places (
    carwash_place_id integer,
    is_free boolean,
    place_id integer,
    carwash_id integer,
    CONSTRAINT carwash_places_pk  PRIMARY KEY (carwash_place_id),
    CONSTRAINT places_fk0 FOREIGN KEY (place_id) REFERENCES places(place_id),
    CONSTRAINT carwashes_fk1 FOREIGN KEY (carwash_id) REFERENCES carwashes(carwash_id)
);
